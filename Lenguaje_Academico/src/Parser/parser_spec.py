import importlib
import ply.yacc as yacc
from Scanner import lexer_spec
importlib.reload(lexer_spec)

tokens = lexer_spec.tokens
get_lexer = lexer_spec.build_lexer

# ================= Estado de ejecución / reporte =================
HUBO_ERROR = False

def _fin_ok():
    # solo “correctamente” si NO hubo errores ni en parser ni en lexer
    if not HUBO_ERROR and not getattr(lexer_spec, "LEXER_HUBO_ERROR", False):
        print("La operación se completó correctamente.")

# ================= Precedencias (aritmética) =================
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
)

# ================= Programa / bloque =================
def p_inicio_marca(p):
    'inicio_marca : KW_INICIO'

def p_programa(p):
    'programa : inicio_marca bloque fin_marca'
    _fin_ok()
    
def p_fin_marca(p):
    '''fin_marca : KW_FIN_PUNTO
                 | KW_FIN
                 | KW_FIN PUNTO'''

def p_bloque(p):
    '''bloque : sentencia bloque
              | '''
    pass

def p_sentencia(p):
    '''sentencia : asignacion
                 | impresion
                 | condicional
                 | repeticion
                 | operacion_lista
                 | definicion_funcion
                 | definicion_procedimiento
                 | llamada_procedimiento'''
    pass

# ================= Asignaciones =================
def p_asignacion_tipada(p):
    'asignacion : KW_ANOTAR tipo ID IGUAL expresion'  

def p_asignacion_inferida(p):
    'asignacion : KW_ANOTAR ID IGUAL expresion'

def p_asignacion_lista_ang(p):
    'asignacion : KW_ANOTAR KW_LISTA MENOR tipo_base MAYOR ID IGUAL KW_VACIA'

def p_asignacion_lista_simple(p):
    'asignacion : KW_ANOTAR KW_LISTA tipo_base ID IGUAL KW_VACIA'  

def p_asignacion_indexada(p):
    'asignacion : KW_ANOTAR ID CORIZQ expresion CORDER IGUAL expresion'

def p_tipo(p):
    '''tipo : KW_NUMERO
            | KW_NOTA
            | KW_ALUMNO
            | KW_BOOL
            | KW_LISTA tipo_base
            | KW_LISTA MENOR tipo_base MAYOR'''
    pass

def p_tipo_base(p):
    '''tipo_base : KW_NUMERO
                 | KW_NOTA
                 | KW_ALUMNO
                 | KW_BOOL'''
    pass

# ================= mostrar =================
def p_impresion(p):
    'impresion : KW_MOSTRAR texto_conc'  

def p_texto_conc(p):
    'texto_conc : elem_texto mas_texto'
    pass

def p_mas_texto(p):
    '''mas_texto : MAS elem_texto mas_texto
                 | '''
    pass

def p_elem_texto(p):
    '''elem_texto : CADENA
                  | ENTERO
                  | booleano
                  | PARIZQ expresion PARDER
                  | ID'''
    pass

# ================= Condicional =================
def p_condicional(p):
    'condicional : KW_EVALUAR condicion bloque_cond'

def p_bloque_cond(p):
    'bloque_cond : KW_SI KW_PASA DOSPUNTOS bloque opc_sino'

def p_opc_sino(p):
    '''opc_sino : KW_SI KW_NOT KW_PASA DOSPUNTOS bloque
                | KW_SINO KW_PASA DOSPUNTOS bloque
                | '''

# ----- Lógica: NOT > AND > OR -----
def p_condicion(p):
    'condicion : cond_o'
    pass

def p_cond_o(p):
    '''cond_o : cond_o KW_OR cond_y
              | cond_o OROP  cond_y
              | cond_y'''
    pass

def p_cond_y(p):
    '''cond_y : cond_y KW_AND cond_no
              | cond_y ANDOP  cond_no
              | cond_no'''
    pass

def p_cond_no(p):
    '''cond_no : KW_NOT cond_no
               | NOTOP  cond_no
               | comparacion'''
    pass

def p_comparacion_rel(p):
    '''comparacion : expresion IGUALIGUAL expresion
                   | expresion DISTINTO   expresion
                   | expresion MENOR      expresion
                   | expresion MENORIGUAL expresion
                   | expresion MAYOR      expresion
                   | expresion MAYORIGUAL expresion'''
    pass

def p_comparacion_entre(p):
    'comparacion : expresion KW_ENTRE expresion KW_AND expresion'
    pass

def p_comparacion_sola(p):
    'comparacion : expresion'
    pass

# ================= Repetición =================
def p_repeticion(p):
    'repeticion : KW_MIENTRAS PARIZQ condicion PARDER KW_HACER bloque'

# ================= Listas =================
def p_operacion_lista_agregar(p):
    'operacion_lista : KW_AGREGAR expresion KW_A ID'

def p_operacion_lista_quitar(p):
    'operacion_lista : KW_QUITAR KW_EN ID CORIZQ expresion CORDER'

def p_operacion_lista_limpiar(p):
    'operacion_lista : KW_LIMPIAR ID'

# ========== Funciones / Procedimientos ==========
def p_definicion_funcion(p):
    'definicion_funcion : KW_FUNCION tipo ID PARIZQ parametros PARDER bloque KW_RETORNAR expresion KW_FIN_FUNCION'

def p_definicion_procedimiento(p):
    'definicion_procedimiento : KW_PROCEDIMIENTO ID PARIZQ parametros PARDER bloque KW_FIN_PROCEDIMIENTO'

def p_llamada_procedimiento(p):
    'llamada_procedimiento : ID PARIZQ argumentos PARDER' 

def p_parametros(p):
    '''parametros : lista_parametros
                  | '''
    pass

def p_lista_parametros(p):
    'lista_parametros : parametro mas_parametros'
    pass

def p_mas_parametros(p):
    '''mas_parametros : COMA parametro mas_parametros
                      | '''
    pass

def p_parametro(p):
    'parametro : tipo ID'
    pass

def p_argumentos(p):
    '''argumentos : lista_argumentos
                  | '''
    pass

def p_lista_argumentos(p):
    'lista_argumentos : expresion mas_argumentos'
    pass

def p_mas_argumentos(p):
    '''mas_argumentos : COMA expresion mas_argumentos
                      | '''
    pass

# ================= Expresiones =================
def p_expresion(p):
    'expresion : termino suma_opt'
    pass

def p_suma_opt(p):
    '''suma_opt : op_suma termino suma_opt
                | '''
    pass

def p_termino(p):
    'termino : factor prod_opt'
    pass

def p_prod_opt(p):
    '''prod_opt : op_mul factor prod_opt
                | '''
    pass

def p_factor(p):
    '''factor : ENTERO
              | CADENA
              | booleano
              | PARIZQ expresion PARDER
              | ID'''
    pass

def p_op_suma(p):
    '''op_suma : MAS
               | MENOS'''
    pass

def p_op_mul(p):
    '''op_mul : POR
              | DIVIDIDO'''
    pass

def p_booleano(p):
    '''booleano : KW_TRUE
                | KW_FALSE'''
    pass

# ================== Errores ==================
def p_error(p):
    global HUBO_ERROR
    HUBO_ERROR = True
    if not p:
        msg = "Token: EOF - Error"
        print(msg)
    else:
        msg = f"Token: {p.value} - Error"
        print(msg)

# ============== Constructor ==============
def build_parser():
    return yacc.yacc(start='programa')