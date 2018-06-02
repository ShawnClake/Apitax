import sys
from antlr4 import *
from apitax.grammar.build.Ah2Lexer import Ah2Lexer
from apitax.grammar.build.Ah2Parser import Ah2Parser
from apitax.grammar.Ah2Listener import Ah2Listener
from apitax.grammar.Ah2Visitor import Ah2Visitor


def main(argv):
    # input = FileStream(argv[1])
    input = FileStream("scripts/test.ah")
    lexer = Ah2Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = Ah2Parser(stream)
    tree = parser.prog()
    printer = Ah2Listener()

    visitor = Ah2Visitor()
    result = visitor.visit(tree)
    # print(result)

    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
