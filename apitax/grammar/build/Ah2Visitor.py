# Generated from D:/Programming/Projects/Apitax/grammar/src\Ah2.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Ah2Parser import Ah2Parser
else:
    from Ah2Parser import Ah2Parser

# This class defines a complete generic visitor for a parse tree produced by Ah2Parser.

class Ah2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Ah2Parser#prog.
    def visitProg(self, ctx:Ah2Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#statements.
    def visitStatements(self, ctx:Ah2Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#statement.
    def visitStatement(self, ctx:Ah2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#expr.
    def visitExpr(self, ctx:Ah2Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#set_var.
    def visitSet_var(self, ctx:Ah2Parser.Set_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#scoping.
    def visitScoping(self, ctx:Ah2Parser.ScopingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#name.
    def visitName(self, ctx:Ah2Parser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#exports.
    def visitExports(self, ctx:Ah2Parser.ExportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#imports.
    def visitImports(self, ctx:Ah2Parser.ImportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#execute.
    def visitExecute(self, ctx:Ah2Parser.ExecuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#inject.
    def visitInject(self, ctx:Ah2Parser.InjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah2Parser#variable_types.
    def visitVariable_types(self, ctx:Ah2Parser.Variable_typesContext):
        return self.visitChildren(ctx)



del Ah2Parser