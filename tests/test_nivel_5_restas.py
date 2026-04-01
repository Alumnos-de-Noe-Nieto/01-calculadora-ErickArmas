from calculadora.validaciones import validar_restas


def test_nivel_5_1_seis_pares_validos():
    """Prueba 5.1: Validar los 6 pares de sustracción válidos."""
    assert validar_restas('IV') is True  # 4 = 5 - 1
    assert validar_restas('IX') is True  # 9 = 10 - 1
    assert validar_restas('XL') is True  # 40 = 50 - 10
    assert validar_restas('XC') is True  # 90 = 100 - 10
    assert validar_restas('CD') is True  # 400 = 500 - 100
    assert validar_restas('CM') is True  # 900 = 1000 - 100


def test_nivel_5_2_no_permitidos():
    """Prueba 5.2: Rechazar sustracciones no estándar."""
    assert validar_restas('IL') is False  # I no puede restar de L
    assert validar_restas('IC') is False  # I no puede restar de C
    assert validar_restas('ID') is False  # I no puede restar de D
    assert validar_restas('IM') is False  # I no puede restar de M

    assert validar_restas('VX') is False  # V no puede restar de X
    assert validar_restas('VL') is False  # V no puede restar de L
    assert validar_restas('VC') is False  # V no puede restar de C
    assert validar_restas('VD') is False  # V no puede restar de D
    assert validar_restas('VM') is False  # V no puede restar de M

    assert validar_restas('XD') is False  # X no puede restar de D
    assert validar_restas('XM') is False  # X no puede restar de M


def test_nivel_5_3_mezcla_valida():
    """Prueba 5.3: Validar combinaciones válidas."""
    assert validar_restas('XIV') is True  # X + (V - I)
    assert validar_restas('XIX') is True  # X + (X - I)
    assert validar_restas('XLV') is True  # (L - X) + V
    assert validar_restas('MCMXCIV') is True  # M + (M - C) + (C - X) + (V - I)


def test_nivel_5_4_solo_aditivos():
    """Prueba 5.4: Validar números puramente aditivos."""
    assert validar_restas('I') is True
    assert validar_restas('V') is True
    assert validar_restas('X') is True
    assert validar_restas('L') is True
    assert validar_restas('C') is True
    assert validar_restas('D') is True
    assert validar_restas('M') is True

    assert validar_restas('MDCLXVI') is True  # 1666
    assert validar_restas('MMM') is True
    assert validar_restas('DCCCLXXXVIII') is True


def test_nivel_5_5_multiples_sustracciones():
    """Prueba 5.5: Validar múltiples sustracciones válidas."""
    assert validar_restas('CDXLIV') is True  # (D - C) + (L - X) + (V - I)
    assert validar_restas('CMXC') is True  # (M - C) + (C - X)
    assert validar_restas('MCMXC') is True  # M + (M - C) + (C - X)
    assert validar_restas('CMXCIX') is True  # (M - C) + (C - X) + (X - I)


def test_nivel_5_6_sustracciones_invalidas_complejas():
    """Prueba 5.6: Rechazar sustracciones inválidas en combinaciones complejas."""
    assert validar_restas('IIX') is False  # II antes de X no es válido
    assert validar_restas('IIV') is False  # II antes de V no es válido
    assert validar_restas('VXIV') is False  # VX no es válido
    assert validar_restas('LC') is False  # L no puede restar de C
    assert validar_restas('DM') is False  # D no puede restar de M


def test_nivel_5_7_complejos():
    """Prueba 5.7: Números romanos complejos."""
    assert validar_restas('MMMCMXCIX') is True  # 3999
    assert validar_restas('MMMDCCCLXXXVIII') is True  # 3888
    assert validar_restas('CCCLXIX') is True  # 369

    assert validar_restas('IL') is False  # IL inválido
    assert validar_restas('IC') is False  # IC inválido
    assert validar_restas('XD') is False  # XD inválido
    assert validar_restas('XM') is False  # XM inválido


def test_nivel_5_8_limites():
    """Prueba 5.8: Casos límite."""
    # Sustracciones válidas exactas
    assert validar_restas('IV') is True
    assert validar_restas('IX') is True
    assert validar_restas('XL') is True
    assert validar_restas('XC') is True
    assert validar_restas('CD') is True
    assert validar_restas('CM') is True

    # Sustracciones inválidas cercanas
    assert validar_restas('IIV') is False
    assert validar_restas('IIX') is False
    assert validar_restas('VX') is False
    assert validar_restas('LC') is False


def test_nivel_5_9_no_afecta_orden():
    """Prueba 5.9: Esta validación solo debe afectar sustracciones, no el orden general."""
    # El orden general es responsabilidad del Nivel 4
    # Aquí solo verificamos que las sustracciones sean válidas
    assert validar_restas('IV') is True  # IV es una sustracción válida
    assert validar_restas('XIV') is True  # XIV tiene una sustracción válida

    # I no puede restar de L, independientemente del orden
    assert validar_restas('IL') is False
