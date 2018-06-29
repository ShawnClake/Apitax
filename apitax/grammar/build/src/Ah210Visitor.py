# Generated from src/Ah210.g4 by ANTLR 4.7.1
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


    # Visit a parse tree produced by Ah210Parser#executers.
    def visitExecuters(self, ctx:Ah210Parser.ExecutersContext):
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


    # Visit a parse tree produced by Ah210Parser#each_statement.
    def visitEach_statement(self, ctx:Ah210Parser.Each_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#condition.
    def visitCondition(self, ctx:Ah210Parser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#block.
    def visitBlock(self, ctx:Ah210Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#callback.
    def visitCallback(self, ctx:Ah210Parser.CallbackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#callback_block.
    def visitCallback_block(self, ctx:Ah210Parser.Callback_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#optional_parameters_block.
    def visitOptional_parameters_block(self, ctx:Ah210Parser.Optional_parameters_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#sig_parameter.
    def visitSig_parameter(self, ctx:Ah210Parser.Sig_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#call_parameter.
    def visitCall_parameter(self, ctx:Ah210Parser.Call_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#optional_parameter.
    def visitOptional_parameter(self, ctx:Ah210Parser.Optional_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#commandtax.
    def visitCommandtax(self, ctx:Ah210Parser.CommandtaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#execute.
    def visitExecute(self, ctx:Ah210Parser.ExecuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#async_execute.
    def visitAsync_execute(self, ctx:Ah210Parser.Async_executeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#await.
    def visitAwait(self, ctx:Ah210Parser.AwaitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#labels.
    def visitLabels(self, ctx:Ah210Parser.LabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#label_comp.
    def visitLabel_comp(self, ctx:Ah210Parser.Label_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#params_statement.
    def visitParams_statement(self, ctx:Ah210Parser.Params_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#options_statement.
    def visitOptions_statement(self, ctx:Ah210Parser.Options_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#delete_statement.
    def visitDelete_statement(self, ctx:Ah210Parser.Delete_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#error_statement.
    def visitError_statement(self, ctx:Ah210Parser.Error_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#return_statement.
    def visitReturn_statement(self, ctx:Ah210Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#login_statement.
    def visitLogin_statement(self, ctx:Ah210Parser.Login_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#endpoint_statement.
    def visitEndpoint_statement(self, ctx:Ah210Parser.Endpoint_statementContext):
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


    # Visit a parse tree produced by Ah210Parser#casting.
    def visitCasting(self, ctx:Ah210Parser.CastingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#auth.
    def visitAuth(self, ctx:Ah210Parser.AuthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#url.
    def visitUrl(self, ctx:Ah210Parser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#log.
    def visitLog(self, ctx:Ah210Parser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#count.
    def visitCount(self, ctx:Ah210Parser.CountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#inject.
    def visitInject(self, ctx:Ah210Parser.InjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#atom.
    def visitAtom(self, ctx:Ah210Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#obj_dict.
    def visitObj_dict(self, ctx:Ah210Parser.Obj_dictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#obj_list.
    def visitObj_list(self, ctx:Ah210Parser.Obj_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#string.
    def visitString(self, ctx:Ah210Parser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#number.
    def visitNumber(self, ctx:Ah210Parser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Ah210Parser#boolean.
    def visitBoolean(self, ctx:Ah210Parser.BooleanContext):
        return self.visitChildren(ctx)



del Ah210Parser