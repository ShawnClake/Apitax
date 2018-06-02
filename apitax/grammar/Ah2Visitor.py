from apitax.grammar.build.Ah2Parser import Ah2Parser
from apitax.grammar.build.Ah2Visitor import Ah2Visitor as Ah2VisitorOriginal
from apitax.ah.scriptax.ScriptData import ScriptData as DataStore
from apitax.logs.Log import Log
import json

class Ah2Visitor(Ah2VisitorOriginal):

    def __init__(self, debug = True):
        self.data = DataStore()
        self.log = Log('logs/log.log')
        self.debug = debug

    # Visit a parse tree produced by Ah2Parser#prog.
    def visitProg(self, ctx):
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

        if (ctx.LPAREN()):
            return self.visit(ctx.expr(0))

        if(ctx.inject()):
            return self.visit(ctx.inject())

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
    def visitSet_var(self, ctx):

        label = ctx.LABEL().getText()

        if (ctx.variable_types()):
            self.data.storeVar(label, self.visit(ctx.variable_types()))

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
        print('imports')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah2Parser#execute.
    def visitExecute(self, ctx):
        print('execute')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by Ah2Parser#inject.
    def visitInject(self, ctx: Ah2Parser.InjectContext):

        label = ""

        if(ctx.DOT_LABEL()):
            label = ctx.DOT_LABEL().getText()

        if(ctx.LABEL()):
            label = ctx.LABEL().getText()

        isRequest = ctx.REQUEST()
        returner = None

        try:
            if (isRequest):
                returner = self.data.getRequest(label)
            else:
                returner = self.data.getVar(label)
        except:
            self.log.error('Injection Failure. Cannot access variable: ' + json.dumps(label) + ' - Does it exist?')
            self.log.log('')
            return None

        if (self.debug):
            self.log.log('> Injecting Variable \'' + label + '\': ' + str(returner))
            self.log.log('')

        return returner


    # Visit a parse tree produced by Ah2Parser#variable.
    def visitVariable_types(self, ctx: Ah2Parser.Variable_typesContext):

        #print('visit variable')

        if (ctx.NUMBER() is not None):
            return float(ctx.NUMBER().getText())

        if (ctx.STRING() is not None):
            return ctx.STRING().getText()[1:-1]

        if (ctx.BOOLEAN() is not None):
            return str(ctx.BOOLEAN().getText()).lower() == "true"

        #print('Impossible Variable')

        # return self.visitChildren(ctx)
