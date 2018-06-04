import sys
from antlr4 import *
from apitax.grammar.build.Ah210Lexer import Ah210Lexer
from apitax.grammar.build.Ah210Parser import Ah210Parser
from apitax.grammar.Ah2Listener import Ah2Listener
from apitax.grammar.Ah2Visitor import Ah2Visitor


def GrammarTest(filepath):
    # input = FileStream(argv[1])
    input = FileStream(filepath)
    lexer = Ah210Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Ah210Parser(stream)
    tree = parser.prog()
    printer = Ah2Listener()

    visitor = Ah2Visitor(None, None)
    result = visitor.visit(tree)
    # print(result)

    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


if __name__ == '__main__':
    GrammarTest(sys.argv)
