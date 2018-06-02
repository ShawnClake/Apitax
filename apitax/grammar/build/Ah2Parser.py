# Generated from D:/Programming/Projects/Apitax/grammar/src\Ah2.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\3\6\3\37\n\3\r\3\16\3 \3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4)\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\62\n\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5=\n\5\f\5\16\5@\13\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6H\n\6\3\7\3\7\3\7\5\7M\n\7")
        buf.write("\3\b\3\b\3\b\5\bR\n\b\3\t\3\t\3\t\5\tW\n\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\5\f`\n\f\3\f\3\f\3\f\3\r\3\r\3\r\2")
        buf.write("\3\b\16\2\4\6\b\n\f\16\20\22\24\26\30\2\6\3\2\5\6\3\2")
        buf.write("\3\4\3\2*+\4\2\23\24..\2l\2\32\3\2\2\2\4\36\3\2\2\2\6")
        buf.write("(\3\2\2\2\b\61\3\2\2\2\nA\3\2\2\2\fL\3\2\2\2\16N\3\2\2")
        buf.write("\2\20S\3\2\2\2\22X\3\2\2\2\24[\3\2\2\2\26]\3\2\2\2\30")
        buf.write("d\3\2\2\2\32\33\5\4\3\2\33\34\7\2\2\3\34\3\3\2\2\2\35")
        buf.write("\37\5\6\4\2\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3")
        buf.write("\2\2\2!\5\3\2\2\2\")\5\26\f\2#)\5\24\13\2$)\5\b\5\2%)")
        buf.write("\5\n\6\2&)\5\f\7\2\')\7/\2\2(\"\3\2\2\2(#\3\2\2\2($\3")
        buf.write("\2\2\2(%\3\2\2\2(&\3\2\2\2(\'\3\2\2\2)\7\3\2\2\2*+\b\5")
        buf.write("\1\2+\62\5\30\r\2,\62\5\26\f\2-.\7\35\2\2./\5\b\5\2/\60")
        buf.write("\7\36\2\2\60\62\3\2\2\2\61*\3\2\2\2\61,\3\2\2\2\61-\3")
        buf.write("\2\2\2\62>\3\2\2\2\63\64\f\5\2\2\64\65\7\7\2\2\65=\5\b")
        buf.write("\5\5\66\67\f\4\2\2\678\t\2\2\28=\5\b\5\59:\f\3\2\2:;\t")
        buf.write("\3\2\2;=\5\b\5\4<\63\3\2\2\2<\66\3\2\2\2<9\3\2\2\2=@\3")
        buf.write("\2\2\2><\3\2\2\2>?\3\2\2\2?\t\3\2\2\2@>\3\2\2\2AB\7$\2")
        buf.write("\2BC\7*\2\2CG\7\b\2\2DH\5\b\5\2EH\5\30\r\2FH\5\24\13\2")
        buf.write("GD\3\2\2\2GE\3\2\2\2GF\3\2\2\2H\13\3\2\2\2IM\5\22\n\2")
        buf.write("JM\5\20\t\2KM\5\16\b\2LI\3\2\2\2LJ\3\2\2\2LK\3\2\2\2M")
        buf.write("\r\3\2\2\2NQ\7!\2\2OR\7*\2\2PR\5\26\f\2QO\3\2\2\2QP\3")
        buf.write("\2\2\2R\17\3\2\2\2SV\7#\2\2TW\7+\2\2UW\5\24\13\2VT\3\2")
        buf.write("\2\2VU\3\2\2\2W\21\3\2\2\2XY\7\"\2\2YZ\5\24\13\2Z\23\3")
        buf.write("\2\2\2[\\\7-\2\2\\\25\3\2\2\2]_\7\33\2\2^`\7)\2\2_^\3")
        buf.write("\2\2\2_`\3\2\2\2`a\3\2\2\2ab\t\4\2\2bc\7\34\2\2c\27\3")
        buf.write("\2\2\2de\t\5\2\2e\31\3\2\2\2\f (\61<>GLQV_")
        return buf.getvalue()


class Ah2Parser ( Parser ):

    grammarFileName = "Ah2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'^'", "'='", 
                     "'>'", "'<'", "'>='", "'<='", "'!='", "'!'", "'_'", 
                     "'.'", "':'", "'%'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'{%'", "'%}'", "'{'", "'}'", "'{{'", 
                     "'}}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "POW", 
                      "EQUAL", "GT", "LT", "GE", "LE", "NE", "NOT", "ULINE", 
                      "DOT", "COLON", "PERCENT", "BOOLEAN", "NUMBER", "INT", 
                      "FLOAT", "EXECUTEOPEN", "EXECUTECLOSE", "BLOCKOPEN", 
                      "BLOCKCLOSE", "MUSTACHEOPEN", "MUSTACHECLOSE", "LPAREN", 
                      "RPAREN", "FALSE", "TRUE", "NAME", "IMPORT", "EXPORT", 
                      "SET", "IF", "THEN", "ELSE", "ENDIF", "REQUEST", "LABEL", 
                      "DOT_LABEL", "HEX", "COMMANDTAX", "STRING", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_expr = 3
    RULE_set_var = 4
    RULE_scoping = 5
    RULE_name = 6
    RULE_exports = 7
    RULE_imports = 8
    RULE_execute = 9
    RULE_inject = 10
    RULE_variable_types = 11

    ruleNames =  [ "prog", "statements", "statement", "expr", "set_var", 
                   "scoping", "name", "exports", "imports", "execute", "inject", 
                   "variable_types" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MUL=3
    DIV=4
    POW=5
    EQUAL=6
    GT=7
    LT=8
    GE=9
    LE=10
    NE=11
    NOT=12
    ULINE=13
    DOT=14
    COLON=15
    PERCENT=16
    BOOLEAN=17
    NUMBER=18
    INT=19
    FLOAT=20
    EXECUTEOPEN=21
    EXECUTECLOSE=22
    BLOCKOPEN=23
    BLOCKCLOSE=24
    MUSTACHEOPEN=25
    MUSTACHECLOSE=26
    LPAREN=27
    RPAREN=28
    FALSE=29
    TRUE=30
    NAME=31
    IMPORT=32
    EXPORT=33
    SET=34
    IF=35
    THEN=36
    ELSE=37
    ENDIF=38
    REQUEST=39
    LABEL=40
    DOT_LABEL=41
    HEX=42
    COMMANDTAX=43
    STRING=44
    NEWLINE=45
    WS=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(Ah2Parser.StatementsContext,0)


        def EOF(self):
            return self.getToken(Ah2Parser.EOF, 0)

        def getRuleIndex(self):
            return Ah2Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = Ah2Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.statements()
            self.state = 25
            self.match(Ah2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Ah2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Ah2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Ah2Parser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = Ah2Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.statement()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Ah2Parser.BOOLEAN) | (1 << Ah2Parser.NUMBER) | (1 << Ah2Parser.MUSTACHEOPEN) | (1 << Ah2Parser.LPAREN) | (1 << Ah2Parser.NAME) | (1 << Ah2Parser.IMPORT) | (1 << Ah2Parser.EXPORT) | (1 << Ah2Parser.SET) | (1 << Ah2Parser.COMMANDTAX) | (1 << Ah2Parser.STRING) | (1 << Ah2Parser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inject(self):
            return self.getTypedRuleContext(Ah2Parser.InjectContext,0)


        def execute(self):
            return self.getTypedRuleContext(Ah2Parser.ExecuteContext,0)


        def expr(self):
            return self.getTypedRuleContext(Ah2Parser.ExprContext,0)


        def set_var(self):
            return self.getTypedRuleContext(Ah2Parser.Set_varContext,0)


        def scoping(self):
            return self.getTypedRuleContext(Ah2Parser.ScopingContext,0)


        def NEWLINE(self):
            return self.getToken(Ah2Parser.NEWLINE, 0)

        def getRuleIndex(self):
            return Ah2Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Ah2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.inject()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.execute()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.set_var()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.scoping()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 37
                self.match(Ah2Parser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_types(self):
            return self.getTypedRuleContext(Ah2Parser.Variable_typesContext,0)


        def inject(self):
            return self.getTypedRuleContext(Ah2Parser.InjectContext,0)


        def LPAREN(self):
            return self.getToken(Ah2Parser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Ah2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Ah2Parser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(Ah2Parser.RPAREN, 0)

        def POW(self):
            return self.getToken(Ah2Parser.POW, 0)

        def MUL(self):
            return self.getToken(Ah2Parser.MUL, 0)

        def DIV(self):
            return self.getToken(Ah2Parser.DIV, 0)

        def PLUS(self):
            return self.getToken(Ah2Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Ah2Parser.MINUS, 0)

        def getRuleIndex(self):
            return Ah2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Ah2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Ah2Parser.BOOLEAN, Ah2Parser.NUMBER, Ah2Parser.STRING]:
                self.state = 41
                self.variable_types()
                pass
            elif token in [Ah2Parser.MUSTACHEOPEN]:
                self.state = 42
                self.inject()
                pass
            elif token in [Ah2Parser.LPAREN]:
                self.state = 43
                self.match(Ah2Parser.LPAREN)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(Ah2Parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = Ah2Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 50
                        self.match(Ah2Parser.POW)
                        self.state = 51
                        self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = Ah2Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 53
                        _la = self._input.LA(1)
                        if not(_la==Ah2Parser.MUL or _la==Ah2Parser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(3)
                        pass

                    elif la_ == 3:
                        localctx = Ah2Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 56
                        _la = self._input.LA(1)
                        if not(_la==Ah2Parser.PLUS or _la==Ah2Parser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(2)
                        pass

             
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Set_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(Ah2Parser.SET, 0)

        def LABEL(self):
            return self.getToken(Ah2Parser.LABEL, 0)

        def EQUAL(self):
            return self.getToken(Ah2Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Ah2Parser.ExprContext,0)


        def variable_types(self):
            return self.getTypedRuleContext(Ah2Parser.Variable_typesContext,0)


        def execute(self):
            return self.getTypedRuleContext(Ah2Parser.ExecuteContext,0)


        def getRuleIndex(self):
            return Ah2Parser.RULE_set_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_var" ):
                listener.enterSet_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_var" ):
                listener.exitSet_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_var" ):
                return visitor.visitSet_var(self)
            else:
                return visitor.visitChildren(self)




    def set_var(self):

        localctx = Ah2Parser.Set_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_set_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(Ah2Parser.SET)
            self.state = 64
            self.match(Ah2Parser.LABEL)
            self.state = 65
            self.match(Ah2Parser.EQUAL)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 66
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 67
                self.variable_types()
                pass

            elif la_ == 3:
                self.state = 68
                self.execute()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ScopingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imports(self):
            return self.getTypedRuleContext(Ah2Parser.ImportsContext,0)


        def exports(self):
            return self.getTypedRuleContext(Ah2Parser.ExportsContext,0)


        def name(self):
            return self.getTypedRuleContext(Ah2Parser.NameContext,0)


        def getRuleIndex(self):
            return Ah2Parser.RULE_scoping

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScoping" ):
                listener.enterScoping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScoping" ):
                listener.exitScoping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScoping" ):
                return visitor.visitScoping(self)
            else:
                return visitor.visitChildren(self)




    def scoping(self):

        localctx = Ah2Parser.ScopingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_scoping)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Ah2Parser.IMPORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.imports()
                pass
            elif token in [Ah2Parser.EXPORT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.exports()
                pass
            elif token in [Ah2Parser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.name()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(Ah2Parser.NAME, 0)

        def LABEL(self):
            return self.getToken(Ah2Parser.LABEL, 0)

        def inject(self):
            return self.getTypedRuleContext(Ah2Parser.InjectContext,0)


        def getRuleIndex(self):
            return Ah2Parser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = Ah2Parser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(Ah2Parser.NAME)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Ah2Parser.LABEL]:
                self.state = 77
                self.match(Ah2Parser.LABEL)
                pass
            elif token in [Ah2Parser.MUSTACHEOPEN]:
                self.state = 78
                self.inject()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExportsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORT(self):
            return self.getToken(Ah2Parser.EXPORT, 0)

        def DOT_LABEL(self):
            return self.getToken(Ah2Parser.DOT_LABEL, 0)

        def execute(self):
            return self.getTypedRuleContext(Ah2Parser.ExecuteContext,0)


        def getRuleIndex(self):
            return Ah2Parser.RULE_exports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExports" ):
                listener.enterExports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExports" ):
                listener.exitExports(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExports" ):
                return visitor.visitExports(self)
            else:
                return visitor.visitChildren(self)




    def exports(self):

        localctx = Ah2Parser.ExportsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exports)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(Ah2Parser.EXPORT)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Ah2Parser.DOT_LABEL]:
                self.state = 82
                self.match(Ah2Parser.DOT_LABEL)
                pass
            elif token in [Ah2Parser.COMMANDTAX]:
                self.state = 83
                self.execute()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImportsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Ah2Parser.IMPORT, 0)

        def execute(self):
            return self.getTypedRuleContext(Ah2Parser.ExecuteContext,0)


        def getRuleIndex(self):
            return Ah2Parser.RULE_imports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImports" ):
                listener.enterImports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImports" ):
                listener.exitImports(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImports" ):
                return visitor.visitImports(self)
            else:
                return visitor.visitChildren(self)




    def imports(self):

        localctx = Ah2Parser.ImportsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_imports)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(Ah2Parser.IMPORT)
            self.state = 87
            self.execute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExecuteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMANDTAX(self):
            return self.getToken(Ah2Parser.COMMANDTAX, 0)

        def getRuleIndex(self):
            return Ah2Parser.RULE_execute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecute" ):
                listener.enterExecute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecute" ):
                listener.exitExecute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecute" ):
                return visitor.visitExecute(self)
            else:
                return visitor.visitChildren(self)




    def execute(self):

        localctx = Ah2Parser.ExecuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_execute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(Ah2Parser.COMMANDTAX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InjectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUSTACHEOPEN(self):
            return self.getToken(Ah2Parser.MUSTACHEOPEN, 0)

        def MUSTACHECLOSE(self):
            return self.getToken(Ah2Parser.MUSTACHECLOSE, 0)

        def DOT_LABEL(self):
            return self.getToken(Ah2Parser.DOT_LABEL, 0)

        def LABEL(self):
            return self.getToken(Ah2Parser.LABEL, 0)

        def REQUEST(self):
            return self.getToken(Ah2Parser.REQUEST, 0)

        def getRuleIndex(self):
            return Ah2Parser.RULE_inject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInject" ):
                listener.enterInject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInject" ):
                listener.exitInject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInject" ):
                return visitor.visitInject(self)
            else:
                return visitor.visitChildren(self)




    def inject(self):

        localctx = Ah2Parser.InjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_inject)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(Ah2Parser.MUSTACHEOPEN)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Ah2Parser.REQUEST:
                self.state = 92
                self.match(Ah2Parser.REQUEST)


            self.state = 95
            _la = self._input.LA(1)
            if not(_la==Ah2Parser.LABEL or _la==Ah2Parser.DOT_LABEL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 96
            self.match(Ah2Parser.MUSTACHECLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_typesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(Ah2Parser.BOOLEAN, 0)

        def NUMBER(self):
            return self.getToken(Ah2Parser.NUMBER, 0)

        def STRING(self):
            return self.getToken(Ah2Parser.STRING, 0)

        def getRuleIndex(self):
            return Ah2Parser.RULE_variable_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_types" ):
                listener.enterVariable_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_types" ):
                listener.exitVariable_types(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_types" ):
                return visitor.visitVariable_types(self)
            else:
                return visitor.visitChildren(self)




    def variable_types(self):

        localctx = Ah2Parser.Variable_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variable_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Ah2Parser.BOOLEAN) | (1 << Ah2Parser.NUMBER) | (1 << Ah2Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




