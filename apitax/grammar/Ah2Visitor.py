from apitax.grammar.build.Ah2Parser import Ah2Parser
from apitax.grammar.build.Ah2Visitor import Ah2Visitor as Ah2VisitorOriginal
from apitax.ah.scriptax.ScriptData import ScriptData as DataStore
from apitax.logs.Log import Log
from apitax.ah.commandtax.commands.Script import Script as ScriptCommand
from apitax.ah.commandtax.Command import Command
import json

class Ah2Visitor(Ah2VisitorOriginal):

    def __init__(self, config, header, debug=True, sensitive=False):
        self.data = DataStore()
        self.log = Log('logs/log.log')
        self.debug = debug
        self.sensitive = sensitive
        self.header = header
        self.config = config
        self.parser = None

    def importCommandRequest(self, request, export=False):

        if (request.getResponseBody().strip() != ''):
            if (isinstance(request, ScriptCommand)):
                self.data.importScriptsExports(request.data, export=export)
            else:
                self.data.storeRequest(request.getResponseBody(), export=export)

    def executeCommand(self, command):
        # setVarContext = Ah2Parser.InjectContext(self.parser)
        # setVarContext.

        return Command(self.header, command, self.config, debug=self.debug, sensitive=self.sensitive).getRequest()

    def getVariable(self, labels, isRequest=False):
        label = self.visit(labels)
        try:
            if (isRequest):
                return self.data.getRequest(label)
            else:
                return self.data.getVar(label)
        except:
            self.log.error('Injection Failure. Cannot access variable: ' + json.dumps(label) + ' - Does it exist?')
            self.log.log('')
            return None

    # Visit a parse tree produced by Ah2Parser#prog.
    def visitProg(self, ctx):
        self.parser = ctx.parser
        temp = self.visitChildren(ctx)
        # print('proj: '+str(temp))
        return temp

    # Visit a parse tree produced by Ah2Parser#statements.
    def visitStatements(self, ctx):
        temp = self.visitChildren(ctx)
        # print('result: '+str(temp))
        return temp

    # Visit a parse tree produced by Ah2Parser#statement.
    def visitStatement(self, ctx):
        line = ctx.getText().strip()
        if(line != ""):
            self.log.log('> Now processing: ' + line)
            self.log.log('')

        temp = self.visitChildren(ctx)
        if (ctx.expr() is not None):
            if (self.debug):
                self.log.log('> Evaluated Expression: ' + str(temp))
                self.log.log('')

        if (line != ""):
            self.log.log('')

        return temp

    # Visit a parse tree produced by Ah2Parser#expr.
    def visitExpr(self, ctx):  # Get number of terms and loop this code for #terms - 1
        if (ctx.variable_types()):
            return self.visit(ctx.variable_types())

        if(ctx.casting()):
            return self.visit(ctx.casting())

        if (ctx.labels()):
            return self.data.getVar(self.visit(ctx.labels()))

        if(ctx.inject()):
            return self.visit(ctx.inject())

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

    # Visit a parse tree produced by Ah2Parser#set_var.
    def visitSet_var(self, ctx: Ah2Parser.Set_varContext):

        label = self.visit(ctx.labels())

        # if (ctx.variable_types()):
        #   self.data.storeVar(label, self.visit(ctx.variable_types()))

        if (ctx.execute()):
            self.data.storeVar(label, self.visit(ctx.execute()))
            # self.variables[ctx.LABEL().getText()] = ctx.COMMANDTAX().getText()

        if(ctx.expr()):
            self.data.storeVar(label, self.visit(ctx.expr()))

        if (self.debug):
            self.log.log('> Assigning Variable: ' + label + ' = ' + str(self.data.getVar(label)))
            self.log.log('')

        # print('set var:')
        # print(self.data.dataStore)

    # Visit a parse tree produced by Ah2Parser#scoping.
    def visitScoping(self, ctx):
        # print('scoping')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah2Parser#name.
    def visitName(self, ctx):
        if ctx.LABEL() is not None:
            self.data.name = ctx.LABEL().getText()

        if ctx.inject() is not None:
            self.data.name = self.visit(ctx.inject())

        if (self.debug):
            self.log.log('> Setting Script Name: ' + self.data.name)
            self.log.log('')

    # Visit a parse tree produced by Ah2Parser#exports.
    def visitExports(self, ctx):
        print('exports')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah2Parser#imports.
    def visitImports(self, ctx):

        request = self.visit(ctx.execute())

        self.importCommandRequest(request)

        if (self.debug):
            self.log.log('> Importing: ' + ctx.getText())
            self.log.log('')

        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah2Parser#execute.
    def visitExecute(self, ctx):
        print('execute')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah2Parser#inject.
    def visitInject(self, ctx: Ah2Parser.InjectContext):

        label = self.visit(ctx.labels())

        returner = self.getVariable(ctx.labels(), isRequest=ctx.REQUEST())

        if (self.debug):
            self.log.log('> Injecting Variable \'' + label + '\': ' + str(returner))
            self.log.log('')

        return returner

    # Visit a parse tree produced by Ah2Parser#variable.
    def visitVariable_types(self, ctx: Ah2Parser.Variable_typesContext):

        # print('visit variable')

        if (ctx.NUMBER() is not None):
            return float(ctx.NUMBER().getText())

        if (ctx.STRING() is not None):
            return ctx.STRING().getText()[1:-1]

        if (ctx.BOOLEAN() is not None):
            return str(ctx.BOOLEAN().getText()).lower() == "true"

        # print('Impossible Variable')

        # return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah2Parser#log.
    def visitLog(self, ctx: Ah2Parser.LogContext):
        if(ctx.STRING()):
            self.log.log('> Logging: ' + json.dumps(ctx.STRING().getText()))
        if (ctx.expr()):
            self.log.log('> Logging: ' + json.dumps(self.visit(ctx.expr())))
        self.log.log('')

    # Visit a parse tree produced by Ah2Parser#labels.
    def visitLabels(self, ctx: Ah2Parser.LabelsContext):
        if(ctx.LABEL()):
            return ctx.LABEL().getText()
        return ctx.DOT_LABEL().getText()

    # Visit a parse tree produced by Ah2Parser#casting.
    def visitCasting(self, ctx:Ah2Parser.CastingContext):
        if(ctx.cast_dict()):
            return self.visit(ctx.cast_dict())

        if(ctx.cast_list()):
            return self.visit(ctx.cast_list())

        if(ctx.cast_num()):
            return self.visit(ctx.cast_num())

        if(ctx.cast_str()):
            return self.visit(ctx.cast_str())

    # Visit a parse tree produced by Ah2Parser#cast_str.
    def visitCast_str(self, ctx:Ah2Parser.Cast_strContext):
        return str(self.getVariable(ctx.labels()))

    # Visit a parse tree produced by Ah2Parser#cast_num.
    def visitCast_num(self, ctx:Ah2Parser.Cast_numContext):
        return float(self.getVariable(ctx.labels()))

    # Visit a parse tree produced by Ah2Parser#cast_dict.
    def visitCast_dict(self, ctx:Ah2Parser.Cast_dictContext):
        return dict(json.loads(str(self.getVariable(ctx.labels()))))

    # Visit a parse tree produced by Ah2Parser#cast_list.
    def visitCast_list(self, ctx:Ah2Parser.Cast_listContext):
        return list(str(self.getVariable(ctx.labels())).split(","))

    # Visit a parse tree produced by Ah2Parser#complex_variables.
    def visitComplex_variables(self, ctx:Ah2Parser.Complex_variablesContext):
        print('we here')
        if(ctx.LIST()):
            return list(str(ctx.STRING().getText()).split(","))
        if (ctx.DICT()):

            return dict(json.loads(str(ctx.STRING().getText())))
