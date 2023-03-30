import ply.lex as lex

literals = [';','=','(',')','{','}','>','<','[',']','+','-','*','/']

tokens = ['WHILE','FOR','IF','ELSE','NUM','FUNCTION','RANGE', 'TYPE', 'IN','VAR','COM','COM_O','COM_E','COM_TEXT']

states = (
    ('COMMENT','exclusive'),
)

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_NUM(t):
    r'\d+'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_RANGE(t):
    r'\.\.'
    return t

def t_TYPE(t):
    r'int|float|char|string|boolean'
    return t

def t_IN(t):
    r'in'
    return t

def t_VAR(t):
    r'[_|aA-zZ][aA-zZ|_|\d]*'
    return t

def t_COM(t):
    r'//.*'
    pass

def t_COM_O(t):
    r'\/\*'
    t.lexer.begin("COMMENT")

def t_COMMENT_COM_E(t):
    r'\*\/'
    t.lexer.begin("INITIAL")

def t_COMMENT_COM_TEXT(t):
    r'.|\n'
    pass

t_ANY_ignore = " \t\n"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

exemplo1 = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

exemplo2 = """
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

exemplo3 = """
/* “Eternos moradores do luzente
Estelífero polo, e claro assento,
Se do grande valor da forte gente
De Luso não perdeis o pensamento,
Deveis de ter sabido claramente,
Como é dos fados grandes certo intento,
Que por ela se esqueçam os humanos
De Assírios, Persas, Gregos e Romanos.” */

//As armas e os barões assinalados,
//Que da ocidental praia Lusitana,
//Por mares nunca de antes navegados,
/*
Passaram ainda além da Taprobana,
Em perigos e guerras esforçados,
Mais do que prometia a força humana,
E entre gente remota edificaram
Novo Reino, que tanto sublimaram;
*/

//Eis ali seus irmãos contra ele vão,
/*(Caso feio e cruel!) mas não se espanta,
Que menos é querer matar o irmão,*/
//Quem contra o Rei e a Pátria se alevanta
"""

exemplos = [exemplo1,exemplo2,exemplo3]

i = 1

for e in exemplos:
    print("Exemplo " + str(i) + ":\n")
    lexer.input(e)
    for tok in lexer:
        print(tok)
    print("+++++++++++++++++++++++++++++++++++++++++++++++\n")
    i+=1
