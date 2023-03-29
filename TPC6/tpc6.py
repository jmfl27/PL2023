import ply.lex as lex

literals = [';','(',')','{','}','>','<','[',']','+','-','*','/']

tokens = ['COM','COM_O','COM_E','COM_TEXT','WHILE','FOR','IF','ELSE','NUM','FUNCTION','VAR','RANGE', 'INT', 'IN']

states = (
    ('COMMENT','exclusive')
)