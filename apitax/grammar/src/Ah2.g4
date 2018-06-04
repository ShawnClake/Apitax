grammar Ah2;

import Ah2Lexer;

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

name : NAME (LABEL | inject);

exports : EXPORT (labels | execute);

imports : IMPORT execute ;

execute : COMMANDTAX (STRING | expr) RPAREN ;

inject : MUSTACHEOPEN REQUEST? labels MUSTACHECLOSE ;

variable_types : BOOLEAN | NUMBER | STRING | complex_variables ;

log : LOG (STRING | expr) RPAREN ;

labels : LABEL | DOT_LABEL ;

casting : cast_dict | cast_list | cast_num | cast_str ;

cast_str : CAST labels COMMA 'str' RPAREN;

cast_num : CAST labels COMMA 'num' RPAREN;

cast_dict : CAST labels COMMA 'dict' RPAREN;

cast_list : CAST labels COMMA 'list' RPAREN;

complex_variables : (LIST | DICT) STRING RPAREN ;






