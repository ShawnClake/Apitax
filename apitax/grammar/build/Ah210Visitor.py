# Generated from D:/Programming/Projects/Apitax/apitax/grammar/src\Ah210.g4 by ANTLR 4.7
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


    # Visit a parse tree produced by Ah210Parser#terminated.
    def visitTerminated(self, ctx:Ah210Parser.TerminatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#non_terminated.
    def visitNon_terminated(self, ctx:Ah210Parser.Non_terminatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#expr.
    def visitExpr(self, ctx:Ah210Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#assignment.
    def visitAssignment(self, ctx:Ah210Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#flow.
    def visitFlow(self, ctx:Ah210Parser.FlowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#if_statement.
    def visitIf_statement(self, ctx:Ah210Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#while_statement.
    def visitWhile_statement(self, ctx:Ah210Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#for_statement.
    def visitFor_statement(self, ctx:Ah210Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#condition.
    def visitCondition(self, ctx:Ah210Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#async_execute.
    def visitAsync_execute(self, ctx:Ah210Parser.Async_executeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#await.
    def visitAwait(self, ctx:Ah210Parser.AwaitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#block.
    def visitBlock(self, ctx:Ah210Parser.BlockContext):
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


    # Visit a parse tree produced by Ah210Parser#url.
    def visitUrl(self, ctx:Ah210Parser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#inject.
    def visitInject(self, ctx:Ah210Parser.InjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#log.
    def visitLog(self, ctx:Ah210Parser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#labels.
    def visitLabels(self, ctx:Ah210Parser.LabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#label_comp.
    def visitLabel_comp(self, ctx:Ah210Parser.Label_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#casting.
    def visitCasting(self, ctx:Ah210Parser.CastingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#string.
    def visitString(self, ctx:Ah210Parser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#boolean.
    def visitBoolean(self, ctx:Ah210Parser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#obj_list.
    def visitObj_list(self, ctx:Ah210Parser.Obj_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#obj_dict.
    def visitObj_dict(self, ctx:Ah210Parser.Obj_dictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#options_statement.
    def visitOptions_statement(self, ctx:Ah210Parser.Options_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#return_statement.
    def visitReturn_statement(self, ctx:Ah210Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#count.
    def visitCount(self, ctx:Ah210Parser.CountContext):
        return self.visitChildren(ctx)



del Ah210Parser