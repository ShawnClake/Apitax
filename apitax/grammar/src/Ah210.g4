grammar Ah210;

//options { tokenVocab=AhLex210; }

/***********
PARSER RULES
***********/

prog : statements EOF ;

statements : statement* ;

statement : 
      terminated
      | non_terminated ;

terminated : 
      (
        execute
        | expr
        | assignment
        | scoping
        | log
        | options_statement
      ) TERMINATOR ;

non_terminated : 
      flow ;

expr :
      labels
      | inject
      | LPAREN expr RPAREN
      | <assoc=right> expr POW expr
      | MINUS expr
      | NOT expr
      | expr (MUL|DIV) expr
      | expr (PLUS|MINUS) expr 
      | expr (GE | LE | GT | LT) expr
      | expr (EQ | NEQ) expr
      | expr AND expr
      | expr OR expr
      | casting
      | variable_types;

assignment : 
      SET labels EQUAL (expr | execute) 
      | labels EQUAL (expr | execute) ;

flow : 
      if_statement
      | while_statement
      | for_statement
      | return_statement;
      
if_statement : IF condition block (ELSE IF condition block)* (ELSE block)? ;

while_statement : WHILE condition block ;

for_statement : FOR labels IN expr block;

condition: LPAREN expr RPAREN ;

block : BLOCKOPEN statements BLOCKCLOSE | statement ;

scoping : imports | exports | name ;

name : NAME expr;

exports : EXPORT (labels | execute);

imports : IMPORT execute ;

execute : COMMANDTAX expr (COMMA expr)* RPAREN ;

inject : MUSTACHEOPEN REQUEST? labels MUSTACHECLOSE ;

variable_types : boolean | NUMBER | string | complex_variables ;

log : LOG expr RPAREN ;

labels : LABEL | DOT_LABEL ;

casting : cast_dict | cast_list | cast_num | cast_str ;

cast_str : CAST expr COMMA 'str' RPAREN ;

cast_num : CAST expr COMMA 'num' RPAREN ;

cast_dict : CAST expr COMMA 'dict' RPAREN ;

cast_list : CAST expr COMMA 'list' RPAREN ;

complex_variables : (LIST | DICT) string RPAREN ;

string : STRING ;

boolean : TRUE | FALSE ;

options_statement : OPTIONS expr ;

return_statement : RETURNS expr? ;








/** OPERATORS **/

GT : '>' ;
LT : '<' ;
GE : '>=' ;
LE : '<=' ;
EQ : '==' ;
NEQ : '!=' ;

PLUS : '+' ;
MINUS : '-' ;
MUL : '*' ;
DIV : '/' ;
POW : '^' ;
EQUAL : '=' ;
NOT: '!' ;
ULINE : '_' ;
DOT : '.' ;
COLON : ':' ;
PERCENT : '%' ;
COMMA : ',' ;

TERMINATOR : ';' ;

NUMBER : INT | FLOAT ; 

INT : '-'?DIGIT+ ;

FLOAT : '-'? DIGIT* DOT DIGIT+ ;


/** BLOCKS **/

EXECUTEOPEN : '{%' ;
EXECUTECLOSE : '%}' ;

MUSTACHEOPEN : '{{' ;
MUSTACHECLOSE : '}}' ;

BLOCKOPEN : '{';
BLOCKCLOSE : '}';

LPAREN : '(';
RPAREN : ')';


/** KEYWORDS **/
AND : A N D ;
OR : O R ;
IN : I N ;
OPTIONS : O P T I O N S ;
RETURNS : R E T U R N ;
FALSE : F A L S E ;
TRUE : T R U E ;
NAME : N A M E ;
IMPORT : I M P O R T ;
EXPORT : E X P O R T ;
SET : S E T ;
IF : I F ;
THEN : T H E N ;
ELSE : E L S E ;
FOR : F O R ;
WHILE : W H I L E ;

COMMANDTAX : C T LPAREN ;
LOG : L O G LPAREN ;
CAST : C A S T LPAREN ;

DICT : D I C T LPAREN ;
LIST : L I S T LPAREN ;

/** KEYCHANGERS **/

REQUEST : R COLON ;

/** TYPES **/

LABEL : (LETTER|ULINE)(LETTER|DIGIT|ULINE)+ ;

DOT_LABEL : (LABEL | DIGIT | DOT)+ ;

HEX : ('0x'|'0X')(HEXDIGIT)HEXDIGIT*;


NEWLINE : '\r'? '\n' -> channel(HIDDEN);
WS : (' ' | '\t')+ -> channel(HIDDEN) ;

BLOCK_COMMENT : DIV MUL .*? MUL DIV -> channel(HIDDEN) ;
LINE_COMMENT : DIV DIV ~[\r\n]* -> channel(HIDDEN) ;

//STRING: '"' (ESC|.)*? '"' ;

STRING : QUOTE (ESC|~["\r\n])*? QUOTE | SQUOTE (ESC|~['\r\n])*? SQUOTE ;



/********
FRAGMENTS
********/
fragment ESC : '\\"' | '\\\'' | '\\\\' ; // 2-char sequences \" and \\

fragment WORDS : (LETTER|DIGIT|ULINE|MINUS|DOT|QUOTE|SQUOTE|LPAREN|RPAREN|':'|'\\'|'/'|'?'|'.'|'!'|','|'#'|'$'|'&'|'@'|' '|'='|'>'|'<'|'('|')'|'['|']'|'{'|'}')+ ;

fragment LETTER : A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z ;

fragment LOWERCASE : [a-z] ;
fragment UPPERCASE : [A-Z] ;

fragment DIGIT : [0-9] ;

fragment A:'A'|'a';    fragment B:'B'|'b';    fragment C:'C'|'c';    fragment D:'D'|'d';    
fragment E:'E'|'e';    fragment F:'F'|'f';    fragment G:'G'|'g';    fragment H:'H'|'h';    
fragment I:'I'|'i';    fragment J:'J'|'j';    fragment K:'K'|'k';    fragment L:'L'|'l';
fragment M:'M'|'m';    fragment N:'N'|'n';    fragment O:'O'|'o';    fragment P:'P'|'p';    
fragment Q:'Q'|'q';    fragment R:'R'|'r';    fragment S:'S'|'s';    fragment T:'T'|'t';    
fragment U:'U'|'u';    fragment V:'V'|'v';    fragment W:'W'|'w';    fragment X:'X'|'x';
fragment Y:'Y'|'y';    fragment Z:'Z'|'z';

fragment QUOTE : '"' ;
fragment SQUOTE : '\'' ;

fragment HEXDIGIT : '0..9'|'a..f'|'A'..'F' ;
