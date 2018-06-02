# Generated from D:/Programming/Projects/NoPatience/API-Middleware/grammar/src\test1.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\24\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\6\3\r\n\3")
        buf.write("\r\3\16\3\16\3\4\3\4\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\3\3")
        buf.write("\2\62;\2\24\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\t\3")
        buf.write("\2\2\2\5\f\3\2\2\2\7\20\3\2\2\2\t\n\7-\2\2\n\4\3\2\2\2")
        buf.write("\13\r\t\2\2\2\f\13\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16")
        buf.write("\17\3\2\2\2\17\6\3\2\2\2\20\21\7\"\2\2\21\22\3\2\2\2\22")
        buf.write("\23\b\4\2\2\23\b\3\2\2\2\4\2\16\3\b\2\2")
        return buf.getvalue()


class test1Lexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    NUMBER = 2
    WHITESPACE = 3

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'+'", "' '"]

    symbolicNames = ["<INVALID>",
                     "NUMBER", "WHITESPACE"]

    ruleNames = ["T__0", "NUMBER", "WHITESPACE"]

    grammarFileName = "test1.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
