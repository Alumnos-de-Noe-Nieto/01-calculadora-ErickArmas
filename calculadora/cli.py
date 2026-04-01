"""
Interfaz de línea de comandos REPL para la calculadora de números romanos.
"""

from calculadora.error import ExpresionInvalida
from calculadora.expresion import evaluar

PROMPT = '🏛 >'
INTRO = """
===========================================================
Calculadora Romana - REPL
============================================================
Ingrese expresiones aritméticas con números romanos.
Ejemplos: "XIV + LX", "X - V", "MMM + D"
Escribe "salir" o "exit" para terminar.
============================================================
"""


def main() -> None:
    """Función principal del REPL de la calculadora."""
    print(INTRO)

    while True:
        try:
            # Leer entrada del usuario
            expresion = input(PROMPT).strip()

            # Verificar comandos de salida
            if not expresion or expresion.lower() in ('salir', 'exit', 'quit'):
                print('¡Adiós!')
                break

            # Calcular resultado
            resultado = evaluar(expresion)
            print(f'Resultado: {resultado}')
            print()

        except ExpresionInvalida as e:
            print(f'Error: {e}')
            print()
        except EOFError:
            # Manejar Ctrl+D
            print('\n¡Adiós!')
            break
        except KeyboardInterrupt:
            # Manejar Ctrl+C
            print('\n¡Adiós!')
            break
        except Exception as e:
            print(f'Error inesperado: {e}')
            print()


if __name__ == '__main__':
    main()
