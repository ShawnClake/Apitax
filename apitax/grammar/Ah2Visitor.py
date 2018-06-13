from apitax.grammar.build.Ah210Parser import Ah210Parser
from apitax.grammar.build.Ah210Visitor import Ah210Visitor as Ah210VisitorOriginal
from apitax.ah.scriptax.ScriptData import ScriptData as DataStore
from apitax.logs.Log import Log
from apitax.utilities.Numbers import isNumber

import json
import re

class Ah2Visitor(Ah210VisitorOriginal):

    SMALL_VALUE = 0.00000000001;

    def __init__(self, config, header, parameters=[], debug=True, sensitive=False):
        self.data = DataStore()
        self.log = Log('logs/log.log')
        self.debug = debug
        self.sensitive = sensitive
        self.header = header
        self.config = config
        self.parser = None
        self.options = {}
        self.data.storeVar("params.passed", parameters)
        
        # Replace the below functionality if possible
        self.regexVar = '{{[ ]{0,}[A-z0-9_.\-]{1,}[ ]{0,}}}'

    def importCommandRequest(self, commandHandler, export=False):
        from apitax.ah.commandtax.commands.Script import Script as ScriptCommand
        
        if (commandHandler.getRequest().getResponseBody().strip() != ''):
            if (isinstance(commandHandler.getRequest(), ScriptCommand)):
                self.data.importScriptsExports(commandHandler.getRequest().parser.data, export=export)
            else:
                self.data.storeRequest(commandHandler.getRequest().getResponseBody(), export=export)

    def executeCommand(self, command, parameters=[]):
        from apitax.ah.commandtax.Commandtax import Commandtax
     
        return Commandtax(self.header, command, self.config, debug=self.debug, sensitive=self.sensitive, parameters=parameters)

    def getVariable(self, label, isRequest=False, convert=True):
        if(convert):
            label = self.visit(label)
        try:
            if (isRequest):
                return self.data.getRequest(label)
            else:
                return self.data.getVar(label)
        except:
            self.log.error('Injection Failure. Cannot access variable: ' + json.dumps(label) + ' - Does it exist?')
            self.log.log('')
            return None

    def useOptions(self):
        if(self.options['params']):

            if(len(self.options['params']) != len(self.data.getVar('params.passed'))):
                errorMessage = 'Insufficient parameters. Expected: ' + str(self.options['params']) + ' but received: ' + str(self.data.getVar('params.passed'))
                self.log.error(errorMessage)
                self.data.setFlow('error', {'message': errorMessage})
            else:
        	
                i = 0
                for param in self.options['params']:
                    self.data.storeVar('params.' + param, self.data.getVar('params.passed.'+str(i)))
                    i += 1
                
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
        # print('proj: '+str(temp))
        return self

    # Visit a parse tree produced by Ah210Parser#statements.
    def visitStatements(self, ctx):
        if(self.data.getFlow('return') or self.data.getFlow('error')):
            return
            
       	self.log.log("")
        temp = self.visitChildren(ctx)
        # print('result: '+str(temp))
        return temp

    # Visit a parse tree produced by Ah210Parser#statement.
    def visitStatement(self, ctx):
        if(self.data.getFlow('return') or self.data.getFlow('error')):
            return
    	
        line = ctx.getText().strip()
        if(line != ""):
            self.log.log('> Now processing: ' + line)
            self.log.log('')

        temp = self.visitChildren(ctx)

        if (line != ""):
            self.log.log('')

        return temp

    # Visit a parse tree produced by Ah210Parser#terminated.
    def visitTerminated(self, ctx:Ah210Parser.TerminatedContext):
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
    def visitNon_terminated(self, ctx:Ah210Parser.Non_terminatedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#expr.
    def visitExpr(self, ctx):  # Get number of terms and loop this code for #terms - 1
        if (ctx.variable_types()):
            return self.visit(ctx.variable_types())

        if(ctx.casting()):
            return self.visit(ctx.casting())

        if (ctx.labels()):
            return self.data.getVar(self.visit(ctx.labels()))

        if(ctx.inject()):
            return self.visit(ctx.inject())
            
        if(ctx.MINUS() and not ctx.expr(1)):
            return self.visit(ctx.expr(0)) * -1
            
        if(ctx.NOT()):
            return not self.visit(ctx.expr(0))
            
        if(ctx.AND()):
            return self.visit(ctx.expr(0)) and self.visit(ctx.expr(1))
            
        if(ctx.OR()):
            return self.visit(ctx.expr(0)) or self.visit(ctx.expr(1))
            
        if(ctx.EQ()):
            return self.visit(ctx.expr(0)) == self.visit(ctx.expr(1))
            
        if(ctx.NEQ()):
            return self.visit(ctx.expr(0)) != self.visit(ctx.expr(1))

        if(ctx.GE()):
            return self.visit(ctx.expr(0)) >= self.visit(ctx.expr(1))
            
        if(ctx.LE()):
            return self.visit(ctx.expr(0)) <= self.visit(ctx.expr(1))
 
        if(ctx.GT()):
            return self.visit(ctx.expr(0)) > self.visit(ctx.expr(1))
            
        if(ctx.LT()):
            return self.visit(ctx.expr(0)) < self.visit(ctx.expr(1))

        if (ctx.LPAREN()):
            return self.visit(ctx.expr(0))

        if (ctx.POW()):
            return self.visit(ctx.expr(0)) ** self.visit(ctx.expr(1))

        if (ctx.PLUS()):
            return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

        if (ctx.MINUS()):
            return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))

        if (ctx.MUL()):
            return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

        if (ctx.DIV()):
            return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))

        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#set_var.
    def visitAssignment(self, ctx:Ah210Parser.AssignmentContext):
        from apitax.ah.commandtax.commands.Script import Script as ScriptCommand
        label = self.visit(ctx.labels())

        if (ctx.execute()):
            commandHandler = self.visit(ctx.execute())['commandHandler']
            returned = None
            if (isinstance(commandHandler.getRequest(), ScriptCommand)):
                returned = commandHandler.getRequest().parser.data.getReturn()
            if(returned is not None):
                self.data.storeVar(label, returned)
            else:
                self.data.storeVar(label, commandHandler.getRequest().getResponseBody())

        if(ctx.expr()):
            self.data.storeVar(label, self.visit(ctx.expr()))

        if (self.debug):
            self.log.log('> Assigning Variable: ' + label + ' = ' + str(self.data.getVar(label)))
            self.log.log('')

    # Visit a parse tree produced by Ah210Parser#flow.
    def visitFlow(self, ctx:Ah210Parser.FlowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#if_statement.
    def visitIf_statement(self, ctx:Ah210Parser.If_statementContext):
    	
        i = 0
        
        while(True):
            if(ctx.condition(i) is None):
                if(ctx.ELSE()):
                    return self.visit(ctx.block(i))
                else:
                    return None
            condition = self.visit(ctx.condition(i))
            if(condition):
                return self.visit(ctx.block(i))
            else:
                i += 1


    # Visit a parse tree produced by Ah210Parser#while_statement.
    def visitWhile_statement(self, ctx:Ah210Parser.While_statementContext):
        while(self.visit(ctx.condition())):
            self.visit(ctx.block())


    # Visit a parse tree produced by Ah210Parser#for_statement.
    def visitFor_statement(self, ctx:Ah210Parser.For_statementContext):
        clause = self.visit(ctx.expr())
        label = self.visit(ctx.labels())
        if(isinstance(clause, list)):
            self.log.log('> Looping through list with var ' + label)
            self.log.log('')
            for item in clause:
                self.log.log('> Assigning ' + label + ' = ' + str(item))
                self.data.storeVar(label, item)
                self.visit(ctx.block())
        
        elif(isinstance(clause, float)):
            self.log.log('> Looping through range with var ' + label)
            self.log.log('')
            for i in range(0, int(clause)):
                self.log.log('> Assigning ' + label + ' = ' + str(i))
                self.data.storeVar(label, i)
                self.visit(ctx.block())
                
        else:
            self.log.error('Invalid Loop Type')
            self.log.log('')



    # Visit a parse tree produced by Ah210Parser#condition.
    def visitCondition(self, ctx:Ah210Parser.ConditionContext):
        condition = self.visit(ctx.expr())
    	
        if (self.debug):
            self.log.log('>> Evaluated Flow Condition as: ' + str(condition))
            self.log.log('')
    	
        return condition

    # Visit a parse tree produced by Ah210Parser#block.
    def visitBlock(self, ctx:Ah210Parser.BlockContext):
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
        
        if(ctx.labels()):
            exportation = self.visit(ctx.labels())
            self.data.exportVar(exportation)
            
        
        if(ctx.execute()):
            request = self.visit(ctx.execute())
            self.importCommandRequest(request['commandHandler'], export=True)
            exportation = request['command']
        
        
        
        if (self.debug):
            self.log.log('> Exporting: ' + exportation)
            self.log.log('')

    # Visit a parse tree produced by Ah210Parser#imports.
    def visitImports(self, ctx):
        
        request = self.visit(ctx.execute())
        self.importCommandRequest(request['commandHandler'])
        
        if (self.debug):
            self.log.log('> Importing: ' + request['command'])
            self.log.log('')

        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah210Parser#execute.
    def visitExecute(self, ctx):
        from apitax.ah.commandtax.commands.Script import Script as ScriptCommand
        command = self.visit(ctx.expr(0))

        parameters = []
        i = 0
        while(ctx.COMMA(i)):
            parameters.append(self.visit(ctx.expr(i+1)))
            i += 1
            
        if (self.debug):
            self.log.log('> Executing Commandtax: \'' + command + '\' ' + 'with parameters: ' + str(parameters))
            self.log.log('')
            
        commandHandler = self.executeCommand(command, parameters=parameters)
        
        if (isinstance(commandHandler.getRequest(), ScriptCommand)): 
            if(commandHandler.getRequest().parser.isError()):
                 self.data.setFlow('error', commandHandler.getRequest().parser.isError())
            
        return dict({"command": command, "commandHandler": commandHandler})

    # Visit a parse tree produced by Ah210Parser#inject.
    def visitInject(self, ctx: Ah210Parser.InjectContext):

        label = self.visit(ctx.labels())

        returner = self.getVariable(ctx.labels(), isRequest=ctx.REQUEST())

        if (self.debug):
            self.log.log('> Injecting Variable \'' + label + '\': ' + str(returner))
            self.log.log('')

        return returner

    # Visit a parse tree produced by Ah210Parser#variable.
    def visitVariable_types(self, ctx: Ah210Parser.Variable_typesContext):

        if (ctx.NUMBER()):
            return float(ctx.NUMBER().getText())

        if (ctx.string()):
            return self.visit(ctx.string())

        if (ctx.boolean()):
            return self.visit(ctx.boolean())
            
        if(ctx.complex_variables()):
            return self.visit(ctx.complex_variables())

    # Visit a parse tree produced by Ah210Parser#boolean.
    def visitBoolean(self, ctx:Ah210Parser.BooleanContext):
        if(ctx.TRUE()):
            return True
        if(ctx.FALSE()):
            return False

    # Visit a parse tree produced by Ah210Parser#log.
    def visitLog(self, ctx: Ah210Parser.LogContext):
        if (ctx.expr()):
            self.log.log('> Logging: ' + json.dumps(self.visit(ctx.expr())))
        self.log.log('')

    # Visit a parse tree produced by Ah210Parser#labels.
    def visitLabels(self, ctx: Ah210Parser.LabelsContext):
        if(ctx.LABEL()):
            return ctx.LABEL().getText()
        return ctx.DOT_LABEL().getText()

    # Visit a parse tree produced by Ah210Parser#casting.
    def visitCasting(self, ctx:Ah210Parser.CastingContext):
        if(ctx.cast_dict()):
            return self.visit(ctx.cast_dict())

        if(ctx.cast_list()):
            return self.visit(ctx.cast_list())

        if(ctx.cast_num()):
            return self.visit(ctx.cast_num())

        if(ctx.cast_str()):
            return self.visit(ctx.cast_str())

    # Visit a parse tree produced by Ah210Parser#cast_str.
    def visitCast_str(self, ctx:Ah210Parser.Cast_strContext):
        value = self.visit(ctx.expr())
        returner = str(value)
        if (self.debug):
            self.log.log('> Casting \'' + str(value) + '\' to string: ' + json.dumps(returner))
            self.log.log('')
        return returner

    # Visit a parse tree produced by Ah210Parser#cast_num.
    def visitCast_num(self, ctx:Ah210Parser.Cast_numContext):
        value = self.visit(ctx.expr())
        returner = float(value)
        if (self.debug):
            self.log.log('> Casting \'' + str(value) + '\' to number: ' + json.dumps(returner))
            self.log.log('')
        return returner

    # Visit a parse tree produced by Ah210Parser#cast_dict.
    def visitCast_dict(self, ctx:Ah210Parser.Cast_dictContext):
        value = self.visit(ctx.expr())
        returner = None
        
        if(isinstance(value, dict)):
            returner = value
        elif(isinstance(value, list)):
            count = 0
            newdict = {}
            for i in value:
                newdict.update({str(count):i})
                count += 1
            returner = dict(newdict)
        else:
            returner = dict({"default": value})
                
        if (self.debug):
            self.log.log('> Casting \'' + str(value) + '\' to dictionary: ' + json.dumps(returner))
            self.log.log('')
                
        return returner

    # Visit a parse tree produced by Ah210Parser#cast_list.
    def visitCast_list(self, ctx:Ah210Parser.Cast_listContext):
        value = self.visit(ctx.expr())
        returner = list(str(value).split(","))
        if (self.debug):
            self.log.log('> Casting \'' + str(value) + '\' to list: ' + json.dumps(returner))
            self.log.log('')
        return returner

    # Visit a parse tree produced by Ah210Parser#complex_variables.
    def visitComplex_variables(self, ctx:Ah210Parser.Complex_variablesContext):
        value = self.visit(ctx.string())
        if(ctx.LIST()):
            return list(str(value).split(","))
        if (ctx.DICT()):
            return dict(json.loads(str(value)))
            
    # Visit a parse tree produced by Ah210Parser#string.
    def visitString(self, ctx:Ah210Parser.StringContext):
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
            if(self.debug):
                self.log.log('> Injecting Variable into String \'' + label + '\': ' + line)
                self.log.log('')
        return line


    # Visit a parse tree produced by Ah210Parser#options_statement.
    def visitOptions_statement(self, ctx:Ah210Parser.Options_statementContext):
        self.options = self.visit(ctx.expr())
        self.useOptions()
        

    # Visit a parse tree produced by Ah210Parser#return_statement.
    def visitReturn_statement(self, ctx:Ah210Parser.Return_statementContext):
        exportation = ""
        if(ctx.expr()):
            exportation = self.visit(ctx.expr())
            self.data.setReturn(exportation)
        else:
            self.data.setReturn({})
        self.data.setFlow('return', True)
        if(self.debug):
            if(exportation != ""):
                self.log.log('> Returning with value: ' + str(exportation))
            else:
                self.log.log('> Returning ')
            self.log.log('')
