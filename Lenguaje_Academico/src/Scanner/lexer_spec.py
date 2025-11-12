import ply.lex as lex

# =========================
# Palabras reservadas
# =========================
CASE_INSENSITIVE = True
reserved = {
    # estructura
    'inicio': 'KW_INICIO',
    'fin': 'KW_FIN',

    # tipos y listas
    'numero': 'KW_NUMERO',
    'nota': 'KW_NOTA',
    'alumno': 'KW_ALUMNO',
    'bool': 'KW_BOOL',
    'lista': 'KW_LISTA',
    'vacia': 'KW_VACIA',

    # booleanos
    'aprobado': 'KW_TRUE',
    'desaprobado': 'KW_FALSE',

    # control / condicional
    'evaluar': 'KW_EVALUAR',
    'si': 'KW_SI',
    'sino': 'KW_SINO',
    'pasa': 'KW_PASA',
    'no': 'KW_NOT',
    'y': 'KW_AND',
    'o': 'KW_OR',
    'entre': 'KW_ENTRE',

    # bucle
    'mientras': 'KW_MIENTRAS',
    'hacer': 'KW_HACER',

    # acciones
    'anotar': 'KW_ANOTAR',
    'mostrar': 'KW_MOSTRAR',

    # listas (ops)
    'agregar': 'KW_AGREGAR',
    'quitar': 'KW_QUITAR',
    'limpiar': 'KW_LIMPIAR',
    'a': 'KW_A',
    'en': 'KW_EN',

    # funciones y procedimientos
    'funcion': 'KW_FUNCION',
    'finfuncion': 'KW_FIN_FUNCION',
    'procedimiento': 'KW_PROCEDIMIENTO',
    'finprocedimiento': 'KW_FIN_PROCEDIMIENTO',
    'retornar': 'KW_RETORNAR',
}

# =========================
# Tokens
# =========================
tokens = (
    'ID', 'ENTERO', 'CADENA',
    # separadores / signos 
    'IGUAL',        # =
    'COMA',         # ,
    'PTCOMA',       # ;
    'PUNTO',        # .
    'PARIZQ', 'PARDER',         # ( )
    'CORIZQ', 'CORDER',         # [ ]
    'LLAVEIZQ', 'LLAVEDER',     # { }
    'DOSPUNTOS',                # :

    # operadores aritméticos
    'MAS', 'MENOS', 'POR', 'DIVIDIDO', 'MOD',   # + - * / %

    # operadores lógicos simbólicos
    'ANDOP', 'OROP', 'NOTOP',                   # && || !

    # comparadores
    'IGUALIGUAL', 'DISTINTO', 'MENORIGUAL', 'MAYORIGUAL', 'MENOR', 'MAYOR',

    # FIN.
    'KW_FIN_PUNTO',
) + tuple(set(reserved.values()))

# =========================
# Reglas
# =========================
# comparadores
t_IGUALIGUAL = r'=='
t_DISTINTO   = r'!='
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='

# simples
t_MENOR      = r'<'
t_MAYOR      = r'>'
t_IGUAL      = r'='
t_COMA       = r','
t_PTCOMA     = r';'
t_PUNTO      = r'\.'
t_DOSPUNTOS  = r':'
t_PARIZQ     = r'\('
t_PARDER     = r'\)'
t_CORIZQ     = r'\['
t_CORDER     = r'\]'
t_LLAVEIZQ   = r'\{'
t_LLAVEDER   = r'\}'
t_MAS        = r'\+'
t_MENOS      = r'-'
t_POR        = r'\*'
t_DIVIDIDO   = r'/'
t_MOD        = r'%'

# lógicos simbólicos
t_ANDOP      = r'&&'
t_OROP       = r'\|\|'
t_NOTOP      = r'!'

# espacios/tabs
t_ignore = ' \t\r'

# =========================
# Reglas por función
# =========================
# Comentarios /*...*/
def t_COMMENT_BLOCK(t):
    r'/\*([^*]|\*+[^*/])*\*+/'
    pass

#//
def t_COMMENT_LINE(t):
    r'//[^\n]*'
    pass

# Numeros
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# String entre ""
def t_CADENA(t):
    r'"([^"\\]|\\.)*"'
    return t

# FIN.
def t_KW_FIN_PUNTO(t):
    r'(?:F|f)(?:I|i)(?:N|n)\.'
    return t

# Identidicadores
def t_ID(t):
    r'[A-Za-z_ÁÉÍÓÚáéíóúñÑ][A-Za-z_0-9ÁÉÍÓÚáéíóúñÑ]*'
    lex = t.value
    key = lex.lower() if CASE_INSENSITIVE else lex
    if key in reserved:
        t.type = reserved[key]
        if t.type == 'KW_TRUE':  t.value = True
        elif t.type == 'KW_FALSE': t.value = False
        else: t.value = lex
    else:
        t.type = 'ID'
        t.value = lex
    return t

#Errores
LEXER_HUBO_ERROR = False

def reset_lexer_error():
    global LEXER_HUBO_ERROR
    LEXER_HUBO_ERROR = False

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    global LEXER_HUBO_ERROR
    LEXER_HUBO_ERROR = True
    print(f"[LEX] Caracter ilegal '{t.value[0]}' en línea {t.lexer.lineno}")
    t.lexer.skip(1)

# =========================
# Constructor
# =========================
def build_lexer():
    return lex.lex()