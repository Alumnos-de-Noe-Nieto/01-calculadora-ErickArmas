from calculadora.validaciones import validar_repeticiones_vld


def test_nivel_3_1_unicos():
    """Prueba 3.1: Validar que V/L/D pueden aparecer individualmente."""
    assert validar_repeticiones_vld('V') is True
    assert validar_repeticiones_vld('L') is True
    assert validar_repeticiones_vld('D') is True


def test_nivel_3_2_exceso_repetido():
    """Prueba 3.2: Rechazar cuando V/L/D se repiten."""
    assert validar_repeticiones_vld('VV') is False
    assert validar_repeticiones_vld('LLL') is False
    assert validar_repeticiones_vld('DD') is False


def test_nivel_3_3_mezcla_valida():
    """Prueba 3.3: Validar cadenas con V/L/D mezclados correctamente."""
    assert validar_repeticiones_vld('VII') is True  # 7
    assert validar_repeticiones_vld('LX') is True  # 60
    assert validar_repeticiones_vld('DC') is True  # 600
    assert validar_repeticiones_vld('MMDCLXVI') is True  # 2666


def test_nivel_3_4_cadenas_sin_vld():
    """Prueba 3.4: Validar cadenas que no contienen V/L/D."""
    assert validar_repeticiones_vld('I') is True
    assert validar_repeticiones_vld('X') is True
    assert validar_repeticiones_vld('C') is True
    assert validar_repeticiones_vld('M') is True
    assert validar_repeticiones_vld('XXX') is True
    assert validar_repeticiones_vld('CCC') is True


def test_nivel_3_5_sustracciones_validas():
    """Prueba 3.5: Validar que las sustracciones con V/L/D sean válidas."""
    assert validar_repeticiones_vld('IV') is True  # I antes de V es válido
    assert validar_repeticiones_vld('IX') is True  # I antes de X es válido
    assert validar_repeticiones_vld('XL') is True  # X antes de L es válido
    assert validar_repeticiones_vld('XC') is True  # X antes de C es válido
    assert validar_repeticiones_vld('CD') is True  # C antes de D es válido
    assert validar_repeticiones_vld('CM') is True  # C antes de M es válido


def test_nivel_3_6_no_afecta_icxm():
    """Prueba 3.6: Esta validación solo debe afectar V/L/D."""
    # I/X/C/M pueden repetirse hasta 3 veces (su validación es responsabilidad del Nivel 2)
    assert validar_repeticiones_vld('III') is True
    assert validar_repeticiones_vld('XXX') is True
    assert validar_repeticiones_vld('CCC') is True
    assert validar_repeticiones_vld('MMM') is True
    assert validar_repeticiones_vld('IIII') is True  # IIII no es problema de Nivel 3


def test_nivel_3_7_complejos():
    """Prueba 3.7: Números romanos complejos."""
    assert validar_repeticiones_vld('MMMCMXCIX') is True  # 3999
    assert validar_repeticiones_vld('MMMDCCCLXXXVIII') is True  # 3888
    assert validar_repeticiones_vld('CCCLXIX') is True  # 369

    assert validar_repeticiones_vld('VV') is False  # VV inválido
    assert validar_repeticiones_vld('LL') is False  # LL inválido
    assert validar_repeticiones_vld('DD') is False  # DD inválido


def test_nivel_3_8_limites():
    """Prueba 3.8: Casos límite."""
    # V/L/D pueden aparecer una sola vez
    assert validar_repeticiones_vld('V') is True
    assert validar_repeticiones_vld('L') is True
    assert validar_repeticiones_vld('D') is True

    # V/L/D no pueden repetirse
    assert validar_repeticiones_vld('VV') is False
    assert validar_repeticiones_vld('LL') is False
    assert validar_repeticiones_vld('DD') is False


def test_nivel_3_9_orden_descendente():
    """Prueba 3.9: Validar en el contexto de orden descendente."""
    assert validar_repeticiones_vld('MDCLXVI') is True  # 1666
    assert validar_repeticiones_vld('MDCCLXVI') is True  # 1766
    assert validar_repeticiones_vld('MMMDCCCLXXXVIII') is True  # 3888

def test_falsos_positivos():
    """
    Los siguientes numeros pasan la validacion de simbolos, pero no son numeros romanos validos aun.
    """
    # Falsos positivos: pasan validación de repeticiones VLD pero no son romanos válidos
    assert validar_repeticiones_vld("VX") is True, "Debe aceptar 'VX' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("VL") is True, "Debe aceptar 'VL' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("VC") is True, "Debe aceptar 'VC' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("VD") is True, "Debe aceptar 'VD' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("LV") is True, "Debe aceptar 'LV' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("LC") is True, "Debe aceptar 'LC' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("LD") is True, "Debe aceptar 'LD' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("DV") is True, "Debe aceptar 'DV' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("DL") is True, "Debe aceptar 'DL' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("DM") is True, "Debe aceptar 'DM' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("IVX") is True, "Debe aceptar 'IVX' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("XLC") is True, "Debe aceptar 'XLC' en validación de VLD, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_vld("CMD") is True, "Debe aceptar 'CMD' en validación de VLD, pero no es romano válido (orden inválido)"
