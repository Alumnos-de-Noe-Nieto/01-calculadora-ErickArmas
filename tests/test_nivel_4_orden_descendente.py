from calculadora.validaciones import validar_orden_descendente


def test_nivel_4_1_aditivos_validos():
    """Prueba 4.1: Validar números aditivos en orden descendente."""
    assert validar_orden_descendente('I') is True
    assert validar_orden_descendente('V') is True
    assert validar_orden_descendente('X') is True
    assert validar_orden_descendente('L') is True
    assert validar_orden_descendente('C') is True
    assert validar_orden_descendente('D') is True
    assert validar_orden_descendente('M') is True

    assert validar_orden_descendente('MDCLXVI') is True  # 1666
    assert validar_orden_descendente('MMM') is True
    assert validar_orden_descendente('DCCCLXXXVIII') is True


def test_nivel_4_2_sustracciones_validas():
    """Prueba 4.2: Validar las 6 sustracciones válidas."""
    assert validar_orden_descendente('IV') is True
    assert validar_orden_descendente('IX') is True
    assert validar_orden_descendente('XL') is True
    assert validar_orden_descendente('XC') is True
    assert validar_orden_descendente('CD') is True
    assert validar_orden_descendente('CM') is True


def test_nivel_4_3_mezcla_valida():
    """Prueba 4.3: Validar combinaciones válidas de aditivos y sustractivos."""
    assert validar_orden_descendente('XIV') is True  # 10 + 4
    assert validar_orden_descendente('XIX') is True  # 10 + 9
    assert validar_orden_descendente('XLV') is True  # 40 + 5
    assert validar_orden_descendente('MCMXCIV') is True  # 1000 + 900 + 90 + 4
    assert validar_orden_descendente('MMMCMXCIX') is True  # 3999


def test_nivel_4_4_orden_invalido():
    """Prueba 4.4: Rechazar orden ascendente incorrecto."""
    assert (
        validar_orden_descendente('IVX') is False
    )  # I(1) < V(5) pero V(5) < X(10) es válido, pero IVX no
    assert validar_orden_descendente('IIV') is False  # II antes de V no es válido
    assert validar_orden_descendente('LC') is False  # L no puede restar de C
    assert validar_orden_descendente('DM') is False  # D no puede restar de M


def test_nivel_4_5_sustracciones_invalidas():
    """Prueba 4.5: Rechazar sustracciones no estándar."""
    assert validar_orden_descendente('IL') is False  # I no puede restar de L
    assert validar_orden_descendente('IC') is False  # I no puede restar de C
    assert validar_orden_descendente('ID') is False  # I no puede restar de D
    assert validar_orden_descendente('IM') is False  # I no puede restar de M

    assert validar_orden_descendente('VX') is False  # V no puede restar de X
    assert validar_orden_descendente('VL') is False  # V no puede restar de L
    assert validar_orden_descendente('VC') is False  # V no puede restar de C
    assert validar_orden_descendente('VD') is False  # V no puede restar de D
    assert validar_orden_descendente('VM') is False  # V no puede restar de M

    assert validar_orden_descendente('XD') is False  # X no puede restar de D
    assert validar_orden_descendente('XM') is False  # X no puede restar de M


def test_nivel_4_6_multiples_sustracciones():
    """Prueba 4.6: Validar múltiples sustracciones válidas."""
    assert validar_orden_descendente('CDXLIV') is True  # 400 + 40 + 4
    assert validar_orden_descendente('CMXC') is True  # 900 + 90
    assert validar_orden_descendente('MCMXC') is True  # 1000 + 900 + 90
    assert validar_orden_descendente('CMXCIX') is True  # 900 + 90 + 9


def test_nivel_4_7_limites():
    """Prueba 4.7: Casos límite."""
    # Orden correcto
    assert validar_orden_descendente('MDCCLXXVI') is True  # 1776

    # Orden incorrecto
    assert (
        validar_orden_descendente('XIVL') is False
    )  # XIV es válido, pero L después no lo es
    assert validar_orden_descendente('ICX') is False  # I antes de C no es válido


def test_nivel_4_8_complejos():
    """Prueba 4.8: Números romanos complejos."""
    assert (
        validar_orden_descendente('MMMCMXCIX') is True
    )  # 3999 (mayor número romano estándar)
    assert validar_orden_descendente('MMMDCCCLXXXVIII') is True  # 3888
    assert validar_orden_descendente('CCCLXIX') is True  # 369

    assert validar_orden_descendente('IIX') is False  # IIX no es válido
    assert validar_orden_descendente('VXIV') is False  # VX no es válido


def test_nivel_4_9_repeticiones_y_orden():
    """Prueba 4.9: Validar repeticiones en orden descendente."""
    # XXXVVVIII tiene múltiples V, lo cual es responsabilidad del Nivel 3
    # El Nivel 4 solo valida el orden descendente, no las repeticiones
    assert validar_orden_descendente('XXXII') is True  # XXX + II = 32
    assert validar_orden_descendente('CCCXXX') is True  # CCC + XXX = 330

def test_falsos_positivos():
    """
    Los siguientes numeros pasan la validacion de simbolos, pero no son numeros romanos validos aun.
    """
    # Falsos positivos: pasan validación de orden descendente pero no son romanos válidos
    assert validar_orden_descendente("IIII") is True, "Debe aceptar 'IIII' en validación de orden descendente, pero no es romano válido (demasiadas I)"
    assert validar_orden_descendente("VV") is True, "Debe aceptar 'VV' en validación de orden descendente, pero no es romano válido (dos V)"
    assert validar_orden_descendente("LL") is True, "Debe aceptar 'LL' en validación de orden descendente, pero no es romano válido (dos L)"
    assert validar_orden_descendente("DD") is True, "Debe aceptar 'DD' en validación de orden descendente, pero no es romano válido (dos D)"
    assert validar_orden_descendente("MMMM") is True, "Debe aceptar 'MMMM' en validación de orden descendente, pero no es romano válido (demasiadas M)"
    assert validar_orden_descendente("XXXX") is True, "Debe aceptar 'XXXX' en validación de orden descendente, pero no es romano válido (demasiadas X)"
    assert validar_orden_descendente("CCCC") is True, "Debe aceptar 'CCCC' en validación de orden descendente, pero no es romano válido (demasiadas C)"


