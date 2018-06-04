/*
 * Parser Rules
 */

 grammar test1;

operation  : NUMBER '+' NUMBER ;

/*
 * Lexer Rules
 */

NUMBER     : [0-9]+ ;

WHITESPACE : ' ' -> skip ;