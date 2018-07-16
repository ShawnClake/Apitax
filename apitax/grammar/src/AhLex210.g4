
lexer grammar AhLex210;

/**********
LEXER RULES
**********/



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


/** KEYCHANGERS **/

REQUEST : R COLON ;

/** TYPES **/

LABEL : (LETTER|ULINE)(LETTER|DIGIT|ULINE)+ ;

DOT_LABEL : (LABEL | DIGIT | DOT)+ ;

//VARIABLE : '{{' LABEL '}}' ;

//DOT_VARIABLE : '{{' DOT_LABEL '}}' ;

//WORD : LETTER+ ;

HEX : ('0x'|'0X')(HEXDIGIT)HEXDIGIT*;


//INLINE_COMMAND : EXECUTEOPEN COMMANDTAX EXECUTECLOSE ;
//INSTANT_COMMAND : COMMANDTAX ;

//

NEWLINE : '\r'? '\n' ;
WS : (' ' | '\t')+ -> channel(HIDDEN) ;

BLOCK_COMMENT : '/*' .*? '*/' -> channel(HIDDEN) ;
LINE_COMMENT : '//' ~[\r\n]* -> channel(HIDDEN) ;

//WS : (' ' | '\t')+ -> channel(HIDDEN) ;


//STRING: '"' (ESC|.)*? '"' ;

//LQUOTE : '"' -> more, mode(STR) ;

//mode STR;
//STRING : '"' -> mode(DEFAULT_MODE) ; // token we want parser to see
//TEXT : . -> more ; // collect more text for string
STRING : QUOTE WORDS QUOTE | SQUOTE WORDS SQUOTE ;


//




/********
FRAGMENTS
********/
fragment ESC : '\\"' | '\\\\' ; // 2-char sequences \" and \\

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