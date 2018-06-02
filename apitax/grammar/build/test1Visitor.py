# Generated from D:/Programming/Projects/NoPatience/API-Middleware/grammar/src\test1.g4 by ANTLR 4.7
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .test1Parser import test1Parser
else:
    from test1Parser import test1Parser


# This class defines a complete generic visitor for a parse tree produced by test1Parser.

class test1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by test1Parser#operation.
    def visitOperation(self, ctx: test1Parser.OperationContext):
        return self.visitChildren(ctx)


del test1Parser
