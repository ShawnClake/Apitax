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
        | execute
        | async_execute
        | expr
        | assignment
        | scoping
        | log
        | url
        | options_statement
        | return_statement
        | await
      ) TERMINATOR ;

non_terminated : 
      flow
 ;

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
      | execute
      | async_execute
      | casting
      | obj_list
      | obj_dict
      | count
      | boolean 
      | NUMBER 
      | string ;

assignment : 
      SET? labels ((
          EQUAL 
          | PE
          | ME
          | MUE
          | DE
      ) expr | D_PLUS | D_MINUS);

flow : 
      if_statement
      | while_statement
      | for_statement ;
      
if_statement : IF condition block (ELSE IF condition block)* (ELSE block)? ;

while_statement : WHILE condition block ;

for_statement : FOR labels IN expr block;

condition: LPAREN expr RPAREN ;

async_execute: (labels EQUAL)? ASYNC execute ;

await: AWAIT labels ;

block : BLOCKOPEN statements BLOCKCLOSE | statement ;

scoping : imports | exports | name ;

name : NAME expr;

exports : EXPORT (labels | execute);

imports : IMPORT execute ;

execute : 
      ( 
        GET 
        | POST 
        | PUT 
        | PATCH 
        | DELETE 
        | COMMANDTAX 
        | SCRIPT 
        | CUSTOM
      ) LPAREN expr (COMMA expr)* RPAREN block? ;

url : URL expr ;

inject : MUSTACHEOPEN REQUEST? labels MUSTACHECLOSE ;

log : LOG LPAREN expr RPAREN ;

labels : label_comp (DOT label_comp)* ;

label_comp : LABEL | inject ;

casting : 
      (
        TYPE_INT
        | TYPE_DEC
        | TYPE_BOOL
        | TYPE_STR
        | TYPE_LIST
        | TYPE_DICT
      ) LPAREN expr RPAREN ;

string : STRING ;

boolean : TRUE | FALSE ;

obj_list : SOPEN expr? (COMMA expr?)* SCLOSE ;

obj_dict : BLOCKOPEN (expr COLON expr)? (COMMA (expr COLON expr)?)* BLOCKCLOSE ; 

options_statement : OPTIONS expr ;

return_statement : RETURNS expr? ;

count : HASH expr ;



/** OPERATORS **/

GT : '>' ;
LT : '<' ;
GE : '>=' ;
LE : '<=' ;
EQ : '==' ;
NEQ : '!=' ;

D_PLUS : '++' ;
D_MINUS : '--' ;
PE : '+=' ;
ME : '-=' ;
MUE : '*=' ;
DE : '/=' ;

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

HASH : '#' ;

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

SOPEN : '[';
SCLOSE : ']';


/** KEYWORDS **/
EACH : E A C H;
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

ASYNC : A S Y N C ;
AWAIT : A W A I T ;

TYPE_INT : I N T ;
TYPE_DICT : D I C T ;
TYPE_LIST : L I S T ;
TYPE_DEC : D E C ;
TYPE_STR : S T R ;
TYPE_BOOL : B O O L ;

COMMANDTAX : C T ;
SCRIPT : S C R I P T ;
CUSTOM : C U S T O M ;

GET : G E T ;
POST : P O S T ;
PUT : P U T ;
PATCH : P A T C H ;
DELETE : D E L E T E ;

URL : U R L ;
LOG : L O G ;

/** KEYCHANGERS **/

REQUEST : R COLON ;

/** TYPES **/

//LABEL : (LETTER|DIGIT|ULINE)+ ;

LABEL : (LETTER | ULINE | DIGIT | DOT)+ (LETTER | ULINE | DIGIT);

HEX : ('0x'|'0X')(HEXDIGIT)HEXDIGIT*;

NEWLINE : '\r'? '\n' -> skip;
WS : (' ' | '\t')+ -> skip ;

BLOCK_COMMENT : DIV MUL .*? MUL DIV -> channel(HIDDEN) ;
LINE_COMMENT : DIV DIV ~[\r\n]* -> channel(HIDDEN) ;

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
