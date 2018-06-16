from apitax.grammar.build.Ah210Parser import Ah210Parser
from apitax.grammar.build.Ah210Visitor import Ah210Visitor as Ah210VisitorOriginal
from apitax.ah.scriptax.ScriptData import ScriptData as DataStore
from apitax.logs.Log import Log
from apitax.utilities.Async import GenericExecution
from apitax.utilities.Json import isJson

import json
import re


class Ah2Visitor(Ah210VisitorOriginal):
    SMALL_VALUE = 0.00000000001;

    def __init__(self, config, header, parameters=[], debug=True, sensitive=False, file=''):
        self.data = DataStore()
        self.log = Log('logs/log.log')
        self.debug = debug
        self.sensitive = sensitive
        self.header = header
        self.config = config
        self.parser = None
        self.options = {}
        self.data.storeVar("params.passed", parameters)
        self.state = {'file': file, 'line': 0, 'char': 0}
        self.threads = []

        # Replace the below functionality if possible
        self.regexVar = '{{[ ]{0,}[A-z0-9_.\-]{1,}[ ]{0,}}}'

    def setState(self, file='', line=-1, char=-1):
        if (file != ''):
            self.state['file'] = file
        if (line != -1):
            self.state['line'] = line
        if (char != -1):
            self.state['char'] = char

    def importCommandRequest(self, commandHandler, export=False):
        from apitax.ah.commandtax.commands.Custom import Custom as CustomCommand

        if (commandHandler.getRequest().getResponseBody().strip() != ''):
            if (not isinstance(commandHandler.getRequest(), CustomCommand)):
                self.data.importScriptsExports(commandHandler.getRequest().parser.data, export=export)
            else:
                self.data.storeRequest(commandHandler.getRequest().getResponseBody(), export=export)

    def executeCommand(self, resolvedCommand, logPrefix = ''):
        from apitax.ah.commandtax.Commandtax import Commandtax

        oldPrefix = self.log.prefix
        self.log.prefix = logPrefix

        if (self.debug):
            self.log.log('> Executing Commandtax: \'' + resolvedCommand['command'] + '\' ' + 'with parameters: ' + str(resolvedCommand['parameters']))
            self.log.log('')

        commandHandler = Commandtax(self.header, resolvedCommand['command'], self.config, debug=self.debug, sensitive=self.sensitive,
                                    parameters=resolvedCommand['parameters'])

        if (hasattr(commandHandler.getRequest(), 'parser')):
            if (commandHandler.getRequest().parser.isError()):
                self.error('Subscript contains error: ' + commandHandler.getRequest().parser.isError())
                # self.data.setFlow('error', commandHandler.getRequest().parser.isError())

        returnResult = commandHandler.getReturnedData()
        if(resolvedCommand['callback']):
            returnResult = self.executeIsolatedCallback(resolvedCommand['callback'], returnResult, logPrefix)

        self.log.prefix = oldPrefix

        return dict({"command": resolvedCommand['command'], "commandHandler": commandHandler, "result": returnResult})

    def getVariable(self, label, isRequest=False, convert=True):
        if (convert):
            label = self.visit(label)
        try:
            if (isRequest):
                return self.data.getRequest(label)
            else:
                return self.data.getVar(label)
        except:

            # self.error('Injection Failure. Cannot access variable: ' + json.dumps(label) + ' - Does it exist?')
            # self.log.log('')
            return None

    def useOptions(self):
        if (self.options['params']):

            if (len(self.options['params']) != len(self.data.getVar('params.passed'))):
                self.error(
                    'Insufficient parameters. Expected: ' + str(self.options['params']) + ' but received: ' + str(
                        self.data.getVar('params.passed')))
                # self.log.error(errorMessage)
                # self.data.setFlow('error', {'message': errorMessage})
            else:

                i = 0
                for param in self.options['params']:
                    self.data.storeVar('params.' + param, self.data.getVar('params.passed.' + str(i)))
                    i += 1

    def inject(self, line):
        matches = re.findall(self.regexVar, line)
        for match in matches:
            label = match[2:-2].strip()
            replacer = self.getVariable(label, convert=False)
            line = line.replace(match, replacer)
        return line

    def executeIsolatedCallback(self, callback, resultScope, logPrefix):
        visitor = Ah2Visitor(self.config, self.header, debug=self.debug,
                             sensitive=self.sensitive)
        visitor.setState(file=self.state['file'])
        visitor.log.prefix = logPrefix
        visitor.data.storeVar('result', resultScope)
        callbackResult = visitor.visit(callback)
        return visitor.data.getVar('result')

    def error(self, message):
        self.data.error(message)

    def isError(self):
        return self.data.getFlow('error')

    def isExit(self):
        return self.data.getFlow('exit')

    def isReturn(self):
        return self.data.getFlow('return')

    # Visit a parse tree produced by Ah210Parser#prog.
    def visitProg(self, ctx):
        self.parser = ctx.parser
        temp = self.visitChildren(ctx)

        if (self.isError()):
            error = self.isError()
            self.log.error(error['message'] + ' in ' + self.state['file'] + ' @' + str(self.state['line']) + ':' + str(
                self.state['char']))
            self.log.log('')
            self.log.log('')

        return self

    # Visit a parse tree produced by Ah210Parser#statements.
    def visitStatements(self, ctx):
        if (self.isReturn() or self.isError()):
            return

        # self.log.log("")
        temp = self.visitChildren(ctx)
        # print('result: '+str(temp))
        return temp

    # Visit a parse tree produced by Ah210Parser#statement.
    def visitStatement(self, ctx):
        if (self.isReturn()):
            return

        if (self.isError()):
            return

        line = ctx.getText().strip()
        if (line != ""):
            self.log.log('> Now processing: ' + line)
            self.log.log('')

        temp = self.visitChildren(ctx)

        if (line != ""):
            self.log.log('')

        self.setState(line=ctx.start.line)  # TODO: Try to add character here as well

        return temp

    # Visit a parse tree produced by Ah210Parser#terminated.
    def visitTerminated(self, ctx: Ah210Parser.TerminatedContext):
        temp = None

        if (ctx.expr() is not None):
            temp = self.visit(ctx.expr())
            if (self.debug):
                self.log.log('> Evaluated Expression: ' + str(temp))
                self.log.log('')
        else:
            temp = self.visitChildren(ctx)

        return temp

    # Visit a parse tree produced by Ah210Parser#non_terminated.
    def visitNon_terminated(self, ctx: Ah210Parser.Non_terminatedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#expr.
    def visitExpr(self, ctx):  # Get number of terms and loop this code for #terms - 1
        if (ctx.execute()):
            resolvedCommand = self.visit(ctx.execute())
            return self.executeCommand(resolvedCommand)['result']

        if (ctx.obj_list()):
            return self.visit(ctx.obj_list())

        if (ctx.obj_dict()):
            return self.visit(ctx.obj_dict())

        if (ctx.NUMBER()):
            return float(ctx.NUMBER().getText())

        if (ctx.string()):
            return self.visit(ctx.string())

        if (ctx.boolean()):
            return self.visit(ctx.boolean())

        if (ctx.casting()):
            return self.visit(ctx.casting())

        if (ctx.count()):
            return self.visit(ctx.count())

        if (ctx.labels()):
            return self.data.getVar(self.visit(ctx.labels()))

        if (ctx.inject()):
            return self.visit(ctx.inject())

        if (ctx.MINUS() and not ctx.expr(1)):
            return self.visit(ctx.expr(0)) * -1

        if (ctx.NOT()):
            return not self.visit(ctx.expr(0))

        if (ctx.AND()):
            return self.visit(ctx.expr(0)) and self.visit(ctx.expr(1))

        if (ctx.OR()):
            return self.visit(ctx.expr(0)) or self.visit(ctx.expr(1))

        if (ctx.EQ()):
            return self.visit(ctx.expr(0)) == self.visit(ctx.expr(1))

        if (ctx.NEQ()):
            return self.visit(ctx.expr(0)) != self.visit(ctx.expr(1))

        if (ctx.GE()):
            return self.visit(ctx.expr(0)) >= self.visit(ctx.expr(1))

        if (ctx.LE()):
            return self.visit(ctx.expr(0)) <= self.visit(ctx.expr(1))

        if (ctx.GT()):
            return self.visit(ctx.expr(0)) > self.visit(ctx.expr(1))

        if (ctx.LT()):
            return self.visit(ctx.expr(0)) < self.visit(ctx.expr(1))

        if (ctx.LPAREN()):
            return self.visit(ctx.expr(0))

        if (ctx.POW()):
            return self.visit(ctx.expr(0)) ** self.visit(ctx.expr(1))

        if (ctx.PLUS()):
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ((isinstance(left, str) and not isinstance(right, str)) or (
                    isinstance(right, str) and not isinstance(left, str))):
                left = str(left)
                right = str(right)
                if (self.debug):
                    self.log.log('> Implicit cast to string: \'' + left + '\' + \'' + right + '\'')
                    self.log.log('')
            return left + right

        if (ctx.MINUS()):
            return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))

        if (ctx.MUL()):
            return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

        if (ctx.DIV()):
            return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))

        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#set_var.
    def visitAssignment(self, ctx: Ah210Parser.AssignmentContext):
        label = self.visit(ctx.labels())
        value = None

        if (ctx.expr()):
            value = self.visit(ctx.expr())

        if (not ctx.EQUAL()):
            var = self.data.getVar(label)
            if (ctx.D_PLUS()):
                value = var + 1
            elif (ctx.D_MINUS()):
                value = var - 1
            else:
                if (ctx.PE()):
                    value += var
                elif (ctx.ME()):
                    value = var - value
                elif (ctx.MUE()):
                    value *= var
                elif (ctx.DE()):
                    value = var / value

        self.data.storeVar(label, value)

        if (self.debug):
            self.log.log('> Assigning Variable: ' + label + ' = ' + str(self.data.getVar(label)))
            self.log.log('')

    # Visit a parse tree produced by Ah210Parser#flow.
    def visitFlow(self, ctx: Ah210Parser.FlowContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#if_statement.
    def visitIf_statement(self, ctx: Ah210Parser.If_statementContext):

        i = 0

        while (True):
            if (ctx.condition(i) is None):
                if (ctx.ELSE()):
                    return self.visit(ctx.block(i))
                else:
                    return None
            condition = self.visit(ctx.condition(i))
            if (condition):
                return self.visit(ctx.block(i))
            else:
                i += 1

    # Visit a parse tree produced by Ah210Parser#while_statement.
    def visitWhile_statement(self, ctx: Ah210Parser.While_statementContext):
        while (self.visit(ctx.condition())):
            self.visit(ctx.block())

    # Visit a parse tree produced by Ah210Parser#for_statement.
    def visitFor_statement(self, ctx: Ah210Parser.For_statementContext):
        clause = self.visit(ctx.expr())
        label = self.visit(ctx.labels())

        if (isinstance(clause, str) and isJson(clause)):
            clause = json.loads(clause)

        if (isinstance(clause, list)):
            if (self.debug):
                self.log.log('> Looping through list with var ' + label)
                self.log.log('')
            for item in clause:
                if (self.debug):
                    self.log.log('>> Assigning ' + label + ' = ' + str(item))
                    self.log.log('')
                    self.log.log('')
                self.data.storeVar(label, item)
                self.visit(ctx.block())
            self.data.deleteVar(label)

        elif (isinstance(clause, float)):
            if (self.debug):
                self.log.log('> Looping through range with var ' + label)
                self.log.log('')
            for i in range(0, int(clause)):
                if (self.debug):
                    self.log.log('>> Assigning ' + label + ' = ' + str(i))
                    self.log.log('')
                    self.log.log('')
                self.data.storeVar(label, i)
                self.visit(ctx.block())
            self.data.deleteVar(label)

        else:
            if (self.debug):
                self.error('Invalid Loop Type: ' + str(type(clause)))
                self.log.log('')

    # Visit a parse tree produced by Ah210Parser#condition.
    def visitCondition(self, ctx: Ah210Parser.ConditionContext):
        condition = self.visit(ctx.expr())

        if (self.debug):
            self.log.log('>> Evaluated Flow Condition as: ' + str(condition))
            self.log.log('')

        return condition

    # Visit a parse tree produced by Ah210Parser#async_execute.
    def visitAsync_execute(self, ctx: Ah210Parser.Async_executeContext):
        label = None
        if (ctx.EQUAL()):
            label = self.visit(ctx.labels())
        resolvedCommand = self.visit(ctx.execute())
        thread = GenericExecution(self, "Async callback", resolvedCommand, log=self.log,
                                  label=label)
        self.threads.append(thread)
        if(label):
            self.data.storeVar(label, thread)
        thread.start()

    # Visit a parse tree produced by Ah210Parser#await.
    def visitAwait(self, ctx: Ah210Parser.AwaitContext):
        thread = self.getVariable(ctx.labels())
        thread.join()

    # Visit a parse tree produced by Ah210Parser#block.
    def visitBlock(self, ctx: Ah210Parser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#scoping.
    def visitScoping(self, ctx):
        # print('scoping')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#name.
    def visitName(self, ctx):
        if ctx.expr():
            self.data.name = self.visit(ctx.expr())

        if (self.debug):
            self.log.log('> Setting Script Name: ' + self.data.name)
            self.log.log('')

    # Visit a parse tree produced by Ah210Parser#exports.
    def visitExports(self, ctx):

        exportation = ""

        if (ctx.labels()):
            exportation = self.visit(ctx.labels())
            self.data.exportVar(exportation)

        if (ctx.execute()):
            resolvedCommand = self.visit(ctx.execute())
            commandHandler = self.executeCommand(resolvedCommand)
            self.importCommandRequest(commandHandler['commandHandler'], export=True)
            exportation = commandHandler['command']

        if (self.debug):
            self.log.log('> Exporting: ' + exportation)
            self.log.log('')

    # Visit a parse tree produced by Ah210Parser#imports.
    def visitImports(self, ctx):

        resolvedCommand = self.visit(ctx.execute())
        commandHandler = self.executeCommand(resolvedCommand)[
            'commandHandler']
        self.importCommandRequest(commandHandler)

        if (self.debug):
            self.log.log('> Importing: ' + resolvedCommand['command'])
            self.log.log('')

        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#execute.
    def visitExecute(self, ctx):
        from apitax.ah.commandtax.commands.Script import Script as ScriptCommand
        firstArg = self.visit(ctx.expr(0))
        command = ""

        if (not ctx.SCRIPT() and not ctx.COMMANDTAX()):
            command += "custom"
            if (ctx.GET()):
                command += " --get"
            if (ctx.POST()):
                command += " --post"
            if (ctx.PUT()):
                command += " --put"
            if (ctx.PATCH()):
                command += " --patch"
            if (ctx.DELETE()):
                command += " --delete"
            command += " --url " + self.data.getUrl("current") + firstArg

        elif (ctx.SCRIPT()):
            command += "script " + firstArg

        elif (ctx.COMMANDTAX()):
            command = firstArg

        if (ctx.expr(1)):
            dataArg = self.visit(ctx.expr(1))
            if ('post' in dataArg):
                command += " --data-post '" + json.dumps(dataArg['post']) + "'"
            if ('query' in dataArg):
                command += " --data-query '" + json.dumps(dataArg['query']) + "'"
            if ('path' in dataArg):
                command += " --data-path '" + json.dumps(dataArg['path']) + "'"
            if ('header' in dataArg):
                command += " --data-header '" + json.dumps(dataArg['header']) + "'"

        parameters = []
        i = 1
        while (ctx.COMMA(i)):
            parameters.append(self.visit(ctx.expr(i + 1)))
            i += 1

        return {'command': command, 'parameters': parameters, 'callback': ctx.block()}

    # Visit a parse tree produced by Ah210Parser#url.
    def visitUrl(self, ctx: Ah210Parser.UrlContext):
        url = self.visit(ctx.expr())
        self.data.storeUrl("current", url)

        if (self.debug):
            self.log.log('> Setting URL: ' + url)
            self.log.log('')

    # Visit a parse tree produced by Ah210Parser#inject.
    def visitInject(self, ctx: Ah210Parser.InjectContext):

        label = self.visit(ctx.labels())

        returner = self.getVariable(ctx.labels(), isRequest=ctx.REQUEST())

        if (self.debug):
            self.log.log('> Injecting Variable \'' + label + '\': ' + str(returner))
            self.log.log('')

        return returner

    # Visit a parse tree produced by Ah210Parser#boolean.
    def visitBoolean(self, ctx: Ah210Parser.BooleanContext):
        if (ctx.TRUE()):
            return True
        if (ctx.FALSE()):
            return False

    # Visit a parse tree produced by Ah210Parser#log.
    def visitLog(self, ctx: Ah210Parser.LogContext):
        if (ctx.expr()):
            self.log.log('> Logging: ' + json.dumps(self.visit(ctx.expr())))
        self.log.log('')

    # Visit a parse tree produced by Ah210Parser#labels.
    def visitLabels(self, ctx: Ah210Parser.LabelsContext):

        label = [self.visit(ctx.label_comp(0))]
        i = 0
        while (ctx.DOT(i)):
            label.append(self.visit(ctx.label_comp(i + 1)))
            i += 1

        return '.'.join(label)

    # Visit a parse tree produced by Ah210Parser#label_comp.
    def visitLabel_comp(self, ctx: Ah210Parser.Label_compContext):
        if (ctx.LABEL()):
            return ctx.LABEL().getText()
        else:
            return self.visit(ctx.inject())

    # Visit a parse tree produced by Ah210Parser#casting.
    def visitCasting(self, ctx: Ah210Parser.CastingContext):
        value = self.visit(ctx.expr())
        if (ctx.TYPE_INT()):
            returner = int(value)
            if (self.debug):
                self.log.log('> Explicitly Casting \'' + str(value) + '\' to int: ' + json.dumps(returner))
                self.log.log('')
            return returner
        if (ctx.TYPE_DEC()):
            returner = float(value)
            if (self.debug):
                self.log.log('> Explicitly Casting \'' + str(value) + '\' to number: ' + json.dumps(returner))
                self.log.log('')
            return returner
        if (ctx.TYPE_BOOL()):
            returner = bool(value)
            if (self.debug):
                self.log.log('> Explicitly Casting \'' + str(value) + '\' to boolean: ' + json.dumps(returner))
                self.log.log('')
            return returner
        if (ctx.TYPE_STR()):
            returner = str(value)
            if (self.debug):
                self.log.log('> Explicitly Casting \'' + str(value) + '\' to string: ' + json.dumps(returner))
                self.log.log('')
            return returner
        if (ctx.TYPE_LIST()):
            returner = list(str(value).split(","))
            if (self.debug):
                self.log.log('> Explicitly Casting \'' + str(value) + '\' to list: ' + json.dumps(returner))
                self.log.log('')
            return returner
        if (ctx.TYPE_DICT()):
            returner = None
            if (isinstance(value, dict)):
                returner = value
            elif (isinstance(value, list)):
                count = 0
                newdict = {}
                for i in value:
                    newdict.update({str(count): i})
                    count += 1
                returner = dict(newdict)
            elif (isinstance(value, str) and isJson(value)):
                returner = dict(json.loads(str(value)))
            else:
                returner = dict({"default": value})
            if (self.debug):
                self.log.log('> Explicitly Casting \'' + str(value) + '\' to dictionary: ' + json.dumps(returner))
                self.log.log('')

        return returner

    # Visit a parse tree produced by Ah210Parser#string.
    def visitString(self, ctx: Ah210Parser.StringContext):
        line = ctx.STRING().getText()[1:-1]
        # print(line)
        line = line.replace('\\"', '"');
        line = line.replace('\\\'', '\'');
        # print(line)
        # line = line.replace("\\\\\"", "\"");
        matches = re.findall(self.regexVar, line)
        for match in matches:
            label = match[2:-2].strip()
            replacer = self.getVariable(label, convert=False)
            line = line.replace(match, replacer)
            if (self.debug):
                self.log.log('> Injecting Variable into String \'' + label + '\': ' + line)
                self.log.log('')
        return line

    # Visit a parse tree produced by Ah210Parser#obj_list.
    def visitObj_list(self, ctx: Ah210Parser.Obj_listContext):
        parameters = []
        i = 0
        if (ctx.expr(0)):
            parameters.append(self.visit(ctx.expr(0)))
        while (ctx.COMMA(i) and ctx.expr(i + 1)):
            parameters.append(self.visit(ctx.expr(i + 1)))
            i += 1
        return parameters

    # Visit a parse tree produced by Ah210Parser#obj_dict.
    def visitObj_dict(self, ctx: Ah210Parser.Obj_dictContext):
        dictionary = {}
        i = 0
        if (ctx.COLON(0)):
            dictionary[self.visit(ctx.expr(0))] = self.visit(ctx.expr(1))
        while (ctx.COMMA(i) and ctx.expr((i + 1) * 2)):
            base = (i + 1) * 2
            dictionary[self.visit(ctx.expr(base))] = self.visit(ctx.expr(base + 1))
            i += 1
        return dictionary

    # Visit a parse tree produced by Ah210Parser#options_statement.
    def visitOptions_statement(self, ctx: Ah210Parser.Options_statementContext):
        self.options = self.visit(ctx.expr())
        self.useOptions()

    # Visit a parse tree produced by Ah210Parser#return_statement.
    def visitReturn_statement(self, ctx: Ah210Parser.Return_statementContext):
        exportation = ""
        if (ctx.expr()):
            exportation = self.visit(ctx.expr())
            self.data.setReturn(exportation)
        else:
            self.data.setReturn({})
        self.data.setFlow('return', True)
        if (self.debug):
            if (exportation != ""):
                self.log.log('> Returning with value: ' + str(exportation))
            else:
                self.log.log('> Returning ')
            self.log.log('')

    # Visit a parse tree produced by Ah210Parser#count.
    def visitCount(self, ctx: Ah210Parser.CountContext):
        return len(self.visit(ctx.expr()))
