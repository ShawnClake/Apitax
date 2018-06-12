# Generated from /home/tsisd/shawn/grammar/src/Ah210.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Ah210Parser import Ah210Parser
else:
    from Ah210Parser import Ah210Parser

# This class defines a complete generic visitor for a parse tree produced by Ah210Parser.

class Ah210Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Ah210Parser#prog.
    def visitProg(self, ctx:Ah210Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#statements.
    def visitStatements(self, ctx:Ah210Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#statement.
    def visitStatement(self, ctx:Ah210Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#expr.
    def visitExpr(self, ctx:Ah210Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#set_var.
    def visitSet_var(self, ctx:Ah210Parser.Set_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#scoping.
    def visitScoping(self, ctx:Ah210Parser.ScopingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#name.
    def visitName(self, ctx:Ah210Parser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#exports.
    def visitExports(self, ctx:Ah210Parser.ExportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#imports.
    def visitImports(self, ctx:Ah210Parser.ImportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#execute.
    def visitExecute(self, ctx:Ah210Parser.ExecuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#inject.
    def visitInject(self, ctx:Ah210Parser.InjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#variable_types.
    def visitVariable_types(self, ctx:Ah210Parser.Variable_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#log.
    def visitLog(self, ctx:Ah210Parser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#labels.
    def visitLabels(self, ctx:Ah210Parser.LabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#casting.
    def visitCasting(self, ctx:Ah210Parser.CastingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#cast_str.
    def visitCast_str(self, ctx:Ah210Parser.Cast_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#cast_num.
    def visitCast_num(self, ctx:Ah210Parser.Cast_numContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#cast_dict.
    def visitCast_dict(self, ctx:Ah210Parser.Cast_dictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#cast_list.
    def visitCast_list(self, ctx:Ah210Parser.Cast_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#complex_variables.
    def visitComplex_variables(self, ctx:Ah210Parser.Complex_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#string.
    def visitString(self, ctx:Ah210Parser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#user_input.
    def visitUser_input(self, ctx:Ah210Parser.User_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#return_statement.
    def visitReturn_statement(self, ctx:Ah210Parser.Return_statementContext):
        return self.visitChildren(ctx)



del Ah210Parser