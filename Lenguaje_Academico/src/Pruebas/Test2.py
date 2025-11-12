import os, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from Scanner.lexer_spec import build_lexer
from Parser.parser_spec import build_parser

# Codigo de prueba - 2
texto = """
INICIO
anotar nota x = 2 + 3
mostrar "Desaprobado"
FIN."""


def run(texto):
    # Scanner
    lexer = build_lexer()
    print("=== TOKENS ===")
    lexer.input(texto)
    while (tok := lexer.token()):
        print(f"{tok.type} -> {tok.value}")
    print()

    # Parser
    print("=== RESULTADO ===")
    parser = build_parser()
    parser.parse(texto, lexer)  

if __name__ == "__main__":
    print ('Inicio del procesamiento')
    print ()
    run(texto)
    print ()
    print ('Fin del procesamiento')
