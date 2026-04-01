import pytest

from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida


def test_nivel_6_1_basicos_romano_a_entero():
    """Prueba 6.1: Conversión básica de romanos a enteros."""
    assert romano_a_entero('I') == 1
    assert romano_a_entero('V') == 5
    assert romano_a_entero('X') == 10
    assert romano_a_entero('L') == 50
    assert romano_a_entero('C') == 100
    assert romano_a_entero('D') == 500
    assert romano_a_entero('M') == 1000


def test_nivel_6_2_aditivos():
    """Prueba 6.2: Conversión de números aditivos."""
    assert romano_a_entero('II') == 2
    assert romano_a_entero('III') == 3
    assert romano_a_entero('VI') == 6
    assert romano_a_entero('VII') == 7
    assert romano_a_entero('VIII') == 8

    assert romano_a_entero('XI') == 11
    assert romano_a_entero('XV') == 15
    assert romano_a_entero('XVI') == 16

    assert romano_a_entero('MDCLXVI') == 1666


def test_nivel_6_3_sustractivos():
    """Prueba 6.3: Conversión de números sustractivos."""
    assert romano_a_entero('IV') == 4
    assert romano_a_entero('IX') == 9
    assert romano_a_entero('XL') == 40
    assert romano_a_entero('XC') == 90
    assert romano_a_entero('CD') == 400
    assert romano_a_entero('CM') == 900


def test_nivel_6_4_mezcla():
    """Prueba 6.4: Conversión de combinaciones."""
    assert romano_a_entero('XIV') == 14
    assert romano_a_entero('XIX') == 19
    assert romano_a_entero('XLV') == 45
    assert romano_a_entero('MCMXCIV') == 1994
    assert romano_a_entero('MMMCMXCIX') == 3999


def test_nivel_6_9_errores_romano_a_entero():
    """Prueba 6.9: Validar que se lancen errores para romanos inválidos."""
    # Símbolos inválidos (ya validado en Nivel 1)
    with pytest.raises(ExpresionInvalida):
        romano_a_entero('ABC')

    # Repeticiones inválidas (ya validado en Nivel 2)
    with pytest.raises(ExpresionInvalida):
        romano_a_entero('IIII')

    # Repeticiones V/L/D (ya validado en Nivel 3)
    with pytest.raises(ExpresionInvalida):
        romano_a_entero('VV')

    # Orden descendente (ya validado en Nivel 4)
    with pytest.raises(ExpresionInvalida):
        romano_a_entero('IVX')

    # Restas inválidas (ya validado en Nivel 5)
    with pytest.raises(ExpresionInvalida):
        romano_a_entero('IL')


def test_nivel_6_casos_representativos():
    """Prueba 6.5: Conversión de casos representativos de números romanos."""
    casos = [
        (1, 'I'),
        (4, 'IV'),
        (9, 'IX'),
        (10, 'X'),
        (40, 'XL'),
        (90, 'XC'),
        (99, 'XCIX'),
        (100, 'C'),
        (400, 'CD'),
        (900, 'CM'),
        (999, 'CMXCIX'),
        (1000, 'M'),
        (1444, 'MCDXLIV'),
        (1994, 'MCMXCIV'),
        (2000, 'MM'),
        (2500, 'MMD'),
        (3000, 'MMM'),
        (3888, 'MMMDCCCLXXXVIII'),
        (3999, 'MMMCMXCIX'),
    ]
    for esperado, romano in casos:
        assert romano_a_entero(romano) == esperado, (
            f'El numero {romano} deberia ser convertido a {esperado}'
        )
