import pytest

from calculadora.error import ExpresionInvalida
from calculadora.expresion import evaluar


def test_nivel_8_1_sumar_basicos():
    """Prueba 8.1: Suma de números romanos básicos."""
    assert evaluar('I + I') == 2
    assert evaluar('V + V') == 10
    assert evaluar('X + X') == 20
    assert evaluar('L + L') == 100
    assert evaluar('C + C') == 200
    assert evaluar('D + D') == 1000
    assert evaluar('M + M') == 2000


def test_nivel_8_2_sumar_complejos():
    """Prueba 8.2: Suma de números romanos complejos."""
    assert evaluar('XIV + LX') == 74  # 14 + 60 = 74
    assert evaluar('XIX + V') == 24  # 19 + 5 = 24
    assert evaluar('XL + X') == 50  # 40 + 10 = 50
    assert evaluar('CM + C') == 1000  # 900 + 100 = 1000
    assert evaluar('IV + VI') == 10  # 4 + 6 = 10
    assert evaluar('MMM + D') == 3500  # 3000 + 500 = 3500


def test_nivel_8_3_sumar_sustractivos():
    """Prueba 8.3: Suma con sustracciones."""
    assert evaluar('IV + VI') == 10  # 4 + 6 = 10
    assert evaluar('IX + I') == 10  # 9 + 1 = 10
    assert evaluar('XL + X') == 50  # 40 + 10 = 50
    assert evaluar('XC + XC') == 180  # 90 + 90 = 180
    assert evaluar('CD + C') == 500  # 400 + 100 = 500
    assert evaluar('CM + C') == 1000  # 900 + 100 = 1000


def test_nivel_8_4a_primer_sumando_invalido():
    """Prueba 8.4a: Primer sumando inválido."""
    with pytest.raises(ExpresionInvalida):
        evaluar('ABC + X')


def test_nivel_8_4b_segundo_sumando_invalido():
    """Prueba 8.4b: Segundo sumando inválido."""
    with pytest.raises(ExpresionInvalida):
        evaluar('X + ABC')


def test_nivel_8_4c_ambos_sumandos_invalidos():
    """Prueba 8.4c: Ambos sumandos inválidos."""
    with pytest.raises(ExpresionInvalida):
        evaluar('IIII + VV')


def test_nivel_8_5_restar_basicos():
    """Prueba 8.5: Resta de números romanos básicos."""
    assert evaluar('X - V') == 5  # 10 - 5 = 5
    assert evaluar('X - I') == 9  # 10 - 1 = 9
    assert evaluar('M - C') == 900  # 1000 - 100 = 900
    assert evaluar('D - C') == 400  # 500 - 100 = 400
    assert evaluar('L - X') == 40  # 50 - 10 = 40


def test_nivel_8_6_restar_complejos():
    """Prueba 8.6: Resta de números romanos complejos."""
    assert evaluar('LXXIV - XIV') == 60  # 74 - 14 = 60
    assert evaluar('XXIV - XIX') == 5  # 24 - 19 = 5
    assert evaluar('M - CM') == 100  # 1000 - 900 = 100
    assert evaluar('MMMCMXCIX - I') == 3998  # 3999 - 1 = 3998


def test_nivel_8_7a_minuendo_invalido():
    """Prueba 8.7a: Minuendo inválido."""
    with pytest.raises(ExpresionInvalida):
        evaluar('ABC - X')


def test_nivel_8_7b_sustraendo_invalido():
    """Prueba 8.7b: Sustraendo inválido."""
    with pytest.raises(ExpresionInvalida):
        evaluar('X - ABC')


def test_nivel_8_7c_resultado_negativo():
    """Prueba 8.7c: Resultado negativo."""
    with pytest.raises(ExpresionInvalida):
        evaluar('V - X')


def test_nivel_8_8_calcular_complejo_unico():
    """Prueba 8.8: Caso único de cálculo complejo (número máximo + 1)."""
    # Este es el único caso único no cubierto en otros tests
    assert evaluar('MMCMXCIX + I') == 3000  # 2999 + 1 = 3000


def test_nivel_8_9a_error_lexico():
    """Prueba 8.9a: Error léxico."""
    with pytest.raises(ExpresionInvalida):
        evaluar('X + A')


def test_nivel_8_9b_error_sintactico():
    """Prueba 8.9b: Error sintáctico."""
    with pytest.raises(ExpresionInvalida):
        evaluar('+ X')


def test_nivel_8_9c_error_semantico():
    """Prueba 8.9c: Error semántico (resultado negativo)."""
    with pytest.raises(ExpresionInvalida):
        evaluar('V - X')


def test_nivel_8_10_pipeline_completo():
    """Prueba 8.10: Pipeline completo de todos los niveles."""
    # Verificar que todas las funciones están integradas correctamente
    assert evaluar('XIV + LX') == 74
    assert evaluar('X - V') == 5

    # Verificar que los errores se propagan correctamente
    with pytest.raises(ExpresionInvalida):
        evaluar('IIII + X')


def test_nivel_8_11_resta_con_sustraccion():
    """Prueba 8.11: Resta que da resultado no romano estándar.

    Estos casos prueban que el sistema calcula enteros correctamente,
    aunque el resultado no sea representable como número romano estándar.
    """
    # Prueba integración de Nivel 6 (conversión) + Nivel 8 (resta)
    # Los resultados 11, 16, 31, 310 no son números romanos estándar
    assert evaluar('XV - IV') == 11  # 15 - 4 = 11
    assert evaluar('XX - IV') == 16  # 20 - 4 = 16
    assert evaluar('XL - IX') == 31  # 40 - 9 = 31
    assert evaluar('CD - XC') == 310  # 400 - 90 = 310


def test_nivel_8_12_resta_limite():
    """Prueba 8.12: Resta que da resultado mínimo (1)."""
    # Prueba el caso límite donde resultado = 1 (mínimo válido)
    assert evaluar('X - IX') == 1  # 10 - 9 = 1
    assert evaluar('V - IV') == 1  # 5 - 4 = 1
    assert evaluar('L - XLIX') == 1  # 50 - 49 = 1


def test_nivel_8_13_expresion_solo_espacios():
    """Prueba 8.13: Expresión con solo espacios.

    Debe lanzar ExpresionInvalida porque después de strip()
    la expresión está vacía.
    """
    # Prueba que el parser maneja correctamente expresiones vacías
    with pytest.raises(ExpresionInvalida):
        evaluar('     ')


def test_nivel_8_14_suma_minima():
    """Prueba 8.14: Suma de números mínimos."""
    # Prueba el caso límite inferior
    assert evaluar('I + I') == 2
    assert evaluar('I + V') == 6
