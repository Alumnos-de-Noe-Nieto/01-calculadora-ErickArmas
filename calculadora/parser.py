"""
Nivel 7: Parsing de Expresiones
Este módulo contiene las funciones para parsear expresiones aritméticas con números romanos.
"""

from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    """
    Representa un token en una expresión aritmética de números romanos.
    """
    tipo: str
    valor: str
    posicion: int


def evaluar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza y valida una expresión aritmética de números romanos.
    """
    # 💡 PISTA: Si la expresión está vacía, retorna lista vacía []
    if not expresion.strip():
        return []

    try:
        # 💡 PISTA: Primero llama a tokenizar_expresion(expresion)
        tokens = tokenizar_expresion(expresion)

        # 💡 PISTA: Luego llama a validar_estructura_tokens(tokens)
        if not validar_estructura_tokens(tokens):
            # 💡 PISTA: Mensaje de error específico
            raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')

        return tokens

    except ExpresionInvalida:
        # Re-lanzamos la excepción para que llegue al REPL
        raise


def tokenizar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza una expresión de texto en una lista de tokens.
    """
    tokens = []
    i = 0

    # 💡 PISTA: Recorre la expresión caracter por caracter con un índice `i` usando while
    while i < len(expresion):
        char = expresion[i]

        # 💡 PISTA: Espacio (' ')
        if char == ' ':
            tokens.append(Token('ESPACIO', ' ', i))
            i += 1
        # 💡 PISTA: Suma ('+')
        elif char == '+':
            tokens.append(Token('SUMA', '+', i))
            i += 1
        # 💡 PISTA: Resta ('-')
        elif char == '-':
            tokens.append(Token('RESTA', '-', i))
            i += 1
        # 💡 PISTA: Romano ('IVXLCDM')
        elif char in 'IVXLCDM':
            # 💡 PISTA: Guarda la posición inicial
            inicio = i
            # 💡 PISTA: Avanza i mientras el caracter sea romano
            while i < len(expresion) and expresion[i] in 'IVXLCDM':
                i += 1
            tokens.append(Token('ROMANO', expresion[inicio:i], inicio))
        # 💡 PISTA: Si el caracter no es ninguno de los anteriores
        else:
            raise ExpresionInvalida(f"Carácter inválido '{char}' en posición {i}")

    return tokens


def validar_estructura_tokens(tokens: list[Token]) -> bool:
    """
    Valida que la expresión tenga una estructura válida.
    """
    # 💡 PISTA: Filtra tokens de tipo 'ESPACIO'
    tokens_limpios = [t for t in tokens if t.tipo != 'ESPACIO']

    # 💡 PISTA: Verifica que haya al menos 3 tokens (ROMANO, OPERADOR, ROMANO)
    # y que el número de tokens sea impar
    if len(tokens_limpios) < 3 or len(tokens_limpios) % 2 == 0:
        return False

    # 💡 PISTA: Verifica que el primer y el último token sean 'ROMANO'
    if tokens_limpios[0].tipo != 'ROMANO' or tokens_limpios[-1].tipo != 'ROMANO':
        return False

    # 💡 PISTA: Recorre los tokens con enumerate para validar alternancia
    for i, token in enumerate(tokens_limpios):
        if i % 2 == 0:
            # 💡 PISTA: Posiciones pares (0, 2, 4...) deben ser 'ROMANO'
            if token.tipo != 'ROMANO':
                return False
        else:
            # 💡 PISTA: Posiciones impares (1, 3, 5...) deben ser 'SUMA' o 'RESTA'
            if token.tipo not in ('SUMA', 'RESTA'):
                return False

    return True
