grammar Ah210;

//options { tokenVocab=AhLex210; }

/***********
PARSER RULES
***********/

prog : statements EOF ;

statements : statement+ ;

statement :
      inject
      | execute
      | expr
      | set_var
      | scoping
      | log
      | return_statement
      | NEWLINE ;

expr :
      variable_types
      | casting
      | labels
      | inject
      | LPAREN expr RPAREN
      | <assoc=right> expr POW expr
      | expr (MUL|DIV) expr
      | expr (PLUS|MINUS) expr ;

set_var : SET labels EQUAL (expr | execute) ;

scoping : imports | exports | name ;

name : NAME expr;

exports : EXPORT (labels | execute);

imports : IMPORT execute ;

execute : COMMANDTAX expr (COMMA expr)* RPAREN ;

inject : MUSTACHEOPEN REQUEST? labels MUSTACHECLOSE ;

variable_types : BOOLEAN | NUMBER | string | complex_variables ;

log : LOG expr RPAREN ;

labels : LABEL | DOT_LABEL ;

casting : cast_dict | cast_list | cast_num | cast_str ;

cast_str : CAST labels COMMA 'str' RPAREN ;

cast_num : CAST labels COMMA 'num' RPAREN ;

cast_dict : CAST labels COMMA 'dict' RPAREN ;

cast_list : CAST labels COMMA 'list' RPAREN ;

complex_variables : (LIST | DICT) string RPAREN ;

string : STRING ;

user_input : INPUT labels COMMA expr COMMA expr (COMMA expr)? RPAREN ; // input(some.destination.var, "The Name of this Input", "A description of the input", "an optional argument which details how to render the field; it falls back to textbox")

return_statement : RETURNS labels? ;








/** OPERATORS **/

PLUS : '+' ;
MINUS : '-' ;
MUL : '*' ;
DIV : '/' ;
POW : '^' ;
EQUAL : '=' ;
GT : '>' ;
LT : '<' ;
GE : '>=' ;
LE : '<=' ;
NE : '!=' ;
NOT: '!' ;
ULINE : '_' ;
DOT : '.' ;
COLON : ':' ;
PERCENT : '%' ;
COMMA : ',' ;

BOOLEAN : TRUE | FALSE ;

NUMBER : INT | FLOAT ; 

INT : '-'?DIGIT+ ;

FLOAT : '-'? DIGIT* DOT DIGIT+ ;


/** BLOCKS **/

EXECUTEOPEN : '{%' ;
EXECUTECLOSE : '%}' ;

BLOCKOPEN : '{';
BLOCKCLOSE : '}';

MUSTACHEOPEN : '{{' ;
MUSTACHECLOSE : '}}' ;

LPAREN : '(';
RPAREN : ')';


/** KEYWORDS **/
RETURNS : R E T U R N ;
FALSE : F A L S E ;
TRUE : T R U E ;
NAME : N A M E ;
IMPORT : I M P O R T ;
EXPORT : E X P O R T ;
SET : S E T;
IF : I F;
THEN : T H E N;
ELSE : E L S E;
ENDIF : E N D I F;


COMMANDTAX : C T LPAREN ;
LOG : L O G LPAREN ;
CAST : C A S T LPAREN ;

DICT : D I C T LPAREN ;
LIST : L I S T LPAREN ;

INPUT : I N P U T LPAREN ;


/** KEYCHANGERS **/

REQUEST : R COLON ;

/** TYPES **/

LABEL : (LETTER|ULINE)(LETTER|DIGIT|ULINE)+ ;

DOT_LABEL : (LABEL | DIGIT | DOT)+ ;

HEX : ('0x'|'0X')(HEXDIGIT)HEXDIGIT*;


NEWLINE : '\r'? '\n' ;
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
