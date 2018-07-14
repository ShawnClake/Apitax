import sys
from antlr4 import *
from apitax.grammar.build.Ah210Lexer import Ah210Lexer
from apitax.grammar.build.Ah210Parser import Ah210Parser
from apitax.grammar.AhListener import AhListener
from apitax.grammar.AhVisitor import AhVisitor


def GrammarTest(filepath):
    # input = FileStream(argv[1])
    input = FileStream(filepath)
    lexer = Ah210Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Ah210Parser(stream)
    tree = parser.prog()
    printer = AhListener()

    visitor = AhVisitor(None, None)
    result = visitor.visit(tree)
    # print(result)

    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


if __name__ == '__main__':
    GrammarTest(sys.argv)
