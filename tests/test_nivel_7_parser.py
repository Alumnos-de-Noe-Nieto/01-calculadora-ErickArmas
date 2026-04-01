import pytest

from calculadora.error import ExpresionInvalida
from calculadora.parser import (
    Token,
    evaluar_expresion,
    tokenizar_expresion,
    validar_estructura_tokens,
)


def test_nivel_7_1_tokenizar_basicos():
    """Prueba 7.1: Tokenización de expresiones básicas."""
    tokens = tokenizar_expresion('XIV + LX')

    assert len(tokens) == 5
    assert tokens[0] == Token('ROMANO', 'XIV', 0)
    assert tokens[1] == Token('ESPACIO', ' ', 3)
    assert tokens[2] == Token('SUMA', '+', 4)
    assert tokens[3] == Token('ESPACIO', ' ', 5)
    assert tokens[4] == Token('ROMANO', 'LX', 6)


def test_nivel_7_2_tokenizar_resta():
    """Prueba 7.2: Tokenización de expresiones con resta."""
    tokens = tokenizar_expresion('X - V')

    assert len(tokens) == 5
    assert tokens[0] == Token('ROMANO', 'X', 0)
    assert tokens[1] == Token('ESPACIO', ' ', 1)
    assert tokens[2] == Token('RESTA', '-', 2)
    assert tokens[3] == Token('ESPACIO', ' ', 3)
    assert tokens[4] == Token('ROMANO', 'V', 4)


def test_nivel_7_3_tokenizar_sin_espacios():
    """Prueba 7.3: Tokenización sin espacios."""
    tokens = tokenizar_expresion('X+V')

    assert len(tokens) == 3
    assert tokens[0] == Token('ROMANO', 'X', 0)
    assert tokens[1] == Token('SUMA', '+', 1)
    assert tokens[2] == Token('ROMANO', 'V', 2)


def test_nivel_7_4_tokenizar_complejos():
    """Prueba 7.4: Tokenización de expresiones complejas."""
    tokens = tokenizar_expresion('MCMXCIV + I')

    assert len(tokens) == 5
    assert tokens[0] == Token('ROMANO', 'MCMXCIV', 0)
    assert tokens[2] == Token('SUMA', '+', 8)
    assert tokens[4] == Token('ROMANO', 'I', 10)


def test_nivel_7_5_tokenizar_errores():
    """Prueba 7.5: Tokenización con caracteres inválidos."""
    with pytest.raises(ExpresionInvalida):
        tokenizar_expresion('X + Y')

    with pytest.raises(ExpresionInvalida):
        tokenizar_expresion('A + B')

    with pytest.raises(ExpresionInvalida):
        tokenizar_expresion('X * V')


def test_nivel_7_6_validar_estructura_valida():
    """Prueba 7.6: Validación de estructura válida."""
    tokens = tokenizar_expresion('XIV + LX')
    assert validar_estructura_tokens(tokens) is True

    tokens = tokenizar_expresion('X - V')
    assert validar_estructura_tokens(tokens) is True

    tokens = tokenizar_expresion('MMM + D')
    assert validar_estructura_tokens(tokens) is True

    # Sin espacios también debe ser válido
    tokens = tokenizar_expresion('X+V')
    assert validar_estructura_tokens(tokens) is True


def test_nivel_7_7_validar_estructura_invalida():
    """Prueba 7.7: Validación de estructura inválida."""
    # Comienza con operador
    tokens = tokenizar_expresion('+ X')
    assert validar_estructura_tokens(tokens) is False

    # Termina con operador
    tokens = tokenizar_expresion('X +')
    assert validar_estructura_tokens(tokens) is False

    # Solo un número
    tokens = [Token('ROMANO', 'X', 0)]
    assert validar_estructura_tokens(tokens) is False

    # Dos operadores consecutivos
    tokens = tokenizar_expresion('X + + V')
    assert validar_estructura_tokens(tokens) is False

    # Solo dos tokens (ROMANO + OPERADOR)
    tokens = [Token('ROMANO', 'X', 0), Token('SUMA', '+', 1)]
    assert validar_estructura_tokens(tokens) is False


def test_nivel_7_8_expresion_vacia():
    """Prueba 7.8: Una expresión vacía es válida y devuelve una lista vacía."""
    tokens = evaluar_expresion('')
    assert tokens == []

    tokens = evaluar_expresion('   ')
    assert tokens == []


def test_nivel_7_9_expresion_espacios():
    """Prueba 7.9: Expresiones con múltiples espacios."""
    tokens = evaluar_expresion('XIV  +   LX')

    # Verificar cantidad de tokens
    assert len(tokens) == 8

    # Verificar tokens principales
    assert tokens[0].tipo == 'ROMANO'  # Primer número
    assert tokens[3].tipo == 'SUMA'  # Operador
    assert tokens[7].tipo == 'ROMANO'  # Segundo número

    # Verificar que los espacios sean ESPACIO (agrupado)
    espacios = [t for t in tokens if t.tipo == 'ESPACIO']
    assert len(espacios) == 5, 'Debería haber 5 tokens de ESPACIO'


def test_nivel_7_10_evaluar_expresion_integracion():
    """Prueba 7.10: Integración completa de evaluar_expresion."""
    # Expresión válida
    tokens = evaluar_expresion('XIV + LX')
    assert len(tokens) == 5
    assert tokens[0].tipo == 'ROMANO'
    assert tokens[2].tipo == 'SUMA'
    assert tokens[4].tipo == 'ROMANO'

    # Expresión inválida por estructura
    with pytest.raises(ExpresionInvalida):
        evaluar_expresion('+ X')

    # Expresión inválida por carácter
    with pytest.raises(ExpresionInvalida):
        evaluar_expresion('X + A')


def test_nivel_7_11_numeros_romanos_complejos():
    """Prueba 7.11: Números romanos complejos en expresiones."""
    tokens = tokenizar_expresion('MMMCMXCIX + I')

    # Verificar que se tokeniza como un solo número romano
    assert tokens[0].tipo == 'ROMANO'
    assert tokens[0].valor == 'MMMCMXCIX'

    tokens = tokenizar_expresion('CDXLIV - X')
    assert tokens[0].tipo == 'ROMANO'
    assert tokens[0].valor == 'CDXLIV'
