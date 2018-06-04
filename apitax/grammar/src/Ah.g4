
grammar Ah;


/***********
PARSER RULES
***********/

prog    :   statements EOF;

statements
:   statement+;

statement
:   assignment | INT
|   NEWLINE;

expr    :   (simple_Expr) (op expr)*;

simple_Expr     : MINUS expr
    | identifier
    | number
    ;

identifier  : VARIABLE;

assignment  : SET identifier EQUAL expr ;

op : PLUS
    |   MINUS
    |   MUL
    |   DIV
    |   EQUAL
    |   GT
    |   LT
    |   GE
    |   LE
    |   NE
    ;

number      : INT
    | FLOAT
    | HEX
                ;



/**********
LEXER RULES
**********/

PLUS    :   '+';
MINUS   :   '-';
MUL    :   '*';
DIV :   '/';
EQUAL  :   '=';
GT  :   '>';
LT  :   '<';
GE  :   '>=';
LE  :   '<=';
NE  :   '!=';
NOT :   '!';
ULINE   :   '_';
DOT :   '.';
//DASH:   '-';

EXECUTEOPEN : '{%' ;
EXECUTECLOSE : '%}' ;

NUMBER : DIGIT+ ([.,] DIGIT+)? ;

WORD                : (LOWERCASE | UPPERCASE | '_')+ ;
 
WHITESPACE : [ \t\r\n]+ -> skip ;
 
NEWLINE             : ('\r'? '\n' | '\r')+ ;

SET :   S E T;
IF  :   I F;
THEN    :   T H E N;
ELSE    :   E L S E;
ENDIF   :   E N D I F;

LABEL   :   (LETTER|ULINE)(LETTER|DIGIT|ULINE)*;

INT     :   '-'?DIGIT+;

FLOAT   :   '-'? DIGIT* DOT DIGIT+;

HEX :   ('0x'|'0X')(HEXDIGIT)HEXDIGIT*;

VARIABLE:    LABEL;


/********
FRAGMENTS
********/

fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;

fragment DIGIT : [0-9] ;

fragment A:'A'|'a';    fragment B:'B'|'b';    fragment C:'C'|'c';    fragment D:'D'|'d';    
fragment E:'E'|'e';    fragment F:'F'|'f';    fragment G:'G'|'g';    fragment H:'H'|'h';    
fragment I:'I'|'i';    fragment J:'J'|'j';    fragment K:'K'|'k';    fragment L:'L'|'l';
fragment M:'M'|'m';    fragment N:'N'|'n';    fragment O:'O'|'o';    fragment P:'P'|'p';    
fragment Q:'Q'|'q';    fragment R:'R'|'r';    fragment S:'S'|'s';    fragment T:'T'|'t';    
fragment U:'U'|'u';    fragment V:'V'|'v';    fragment W:'W'|'w';    fragment X:'X'|'x';
fragment Y:'Y'|'y';    fragment Z:'Z'|'z';


fragment LETTER
:   A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z;

fragment HEXDIGIT   
:   '0..9'|'a..f'|'A'..'F';






