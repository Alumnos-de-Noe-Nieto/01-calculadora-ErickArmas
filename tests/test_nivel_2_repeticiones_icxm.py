from calculadora.validaciones import validar_repeticiones_icxm


def test_nivel_2_1_triunfo_cesar():
    """Prueba 2.1: Validar que I/X/C/M pueden repetirse hasta 3 veces."""

    assert validar_repeticiones_icxm('I') is True, "El numero romano 'I' debería ser válido."
    assert validar_repeticiones_icxm('II') is True, "El numero romano 'II' debería ser válido."
    assert validar_repeticiones_icxm('III') is True

    assert validar_repeticiones_icxm('X') is True
    assert validar_repeticiones_icxm('XX') is True
    assert validar_repeticiones_icxm('XXX') is True

    assert validar_repeticiones_icxm('C') is True
    assert validar_repeticiones_icxm('CC') is True
    assert validar_repeticiones_icxm('CCC') is True

    assert validar_repeticiones_icxm('M') is True
    assert validar_repeticiones_icxm('MM') is True
    assert validar_repeticiones_icxm('MMM') is True


def test_nivel_2_2_exceso_legionario():
    """Prueba 2.2: Rechazar cuando I/X/C/M se repiten más de 3 veces."""
    assert validar_repeticiones_icxm('IIII') is False
    assert validar_repeticiones_icxm('XXXX') is False
    assert validar_repeticiones_icxm('CCCC') is False
    assert validar_repeticiones_icxm('MMMM') is False


def test_nivel_2_3_mezcla_valida():
    """Prueba 2.3: Validar cadenas con mezcla de repeticiones válidas."""
    assert validar_repeticiones_icxm('XXXVII') is True  # 37
    assert validar_repeticiones_icxm('CCCXX') is True  # 320
    assert validar_repeticiones_icxm('MMMCD') is True  # 3400


def test_nivel_2_4_multiples_repeticiones_validas():
    """Prueba 2.4: Validar cadenas con múltiples grupos de repeticiones válidas."""
    # Esta validación solo afecta I/X/C/M, V/L/D se validan en Nivel 3
    assert (
        validar_repeticiones_icxm('XXXVIII') is True
    )  # XXX + VIII (VIII es V + III, solo III se valida aquí)
    assert validar_repeticiones_icxm('XXXII') is True  # XXX + II = 32
    assert validar_repeticiones_icxm('CCCXXX') is True  # CCC + XXX = 330


def test_nivel_2_5_repeticiones_aisladas():
    """Prueba 2.5: Validar repeticiones que no están al inicio."""
    assert validar_repeticiones_icxm('XIII') is True  # XIII = 13
    assert validar_repeticiones_icxm('CXXX') is True  # CXXX = 130
    assert validar_repeticiones_icxm('MCCC') is True  # MCCC = 1300

    assert validar_repeticiones_icxm('XIV') is True  # XIV = 14 (no es repetición)
    assert validar_repeticiones_icxm('CXL') is True  # CXL = 140


def test_nivel_2_6_limites():
    """Prueba 2.6: Casos límite."""
    # Repeticiones exactamente en el límite
    assert validar_repeticiones_icxm('III') is True
    assert validar_repeticiones_icxm('XXX') is True
    assert validar_repeticiones_icxm('CCC') is True
    assert validar_repeticiones_icxm('MMM') is True

    # Repeticiones justo encima del límite
    assert validar_repeticiones_icxm('IIII') is False
    assert validar_repeticiones_icxm('XXXX') is False
    assert validar_repeticiones_icxm('CCCC') is False
    assert validar_repeticiones_icxm('MMMM') is False


def test_nivel_2_7_complejos():
    """Prueba 2.7: Números romanos complejos."""
    assert validar_repeticiones_icxm('MMMCMXCIX') is True  # 3999
    assert validar_repeticiones_icxm('MMMDCCCLXXXVIII') is True  # 3888
    assert validar_repeticiones_icxm('CCCLXIX') is True  # 369

    assert validar_repeticiones_icxm('MMMMCMXCIX') is False  # MMMM inválido
    assert validar_repeticiones_icxm('MMMCCCC') is False  # CCCC inválido


def test_nivel_2_8_no_afecta_otros_simbolos():
    """Prueba 2.8: Esta validación solo debe afectar I/X/C/M."""
    # V/L/D pueden aparecer (su validación es responsabilidad del Nivel 3)
    assert (
        validar_repeticiones_icxm('VV') is True
    )  # V se repite pero Nivel 2 no lo valida
    assert (
        validar_repeticiones_icxm('LL') is True
    )  # L se repite pero Nivel 2 no lo valida
    assert (
        validar_repeticiones_icxm('DD') is True
    )  # D se repite pero Nivel 2 no lo valida


def test_falsos_positivos():
    """
    Los siguientes numeros pasan la validacion de IXCM, pero no son numeros romanos validos aun.
    """
    # Falsos positivos: pasan validación de repeticiones IXCM pero no son romanos válidos
    assert validar_repeticiones_icxm("VV") is True, "Debe aceptar 'VV' en validación de IXCM, pero no es romano válido (dos V)"
    assert validar_repeticiones_icxm("LL") is True, "Debe aceptar 'LL' en validación de IXCM, pero no es romano válido (dos L)"
    assert validar_repeticiones_icxm("DD") is True, "Debe aceptar 'DD' en validación de IXCM, pero no es romano válido (dos D)"
    assert validar_repeticiones_icxm("VLV") is True, "Debe aceptar 'VLV' en validación de IXCM, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_icxm("IVI") is True, "Debe aceptar 'IVI' en validación de IXCM, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_icxm("XIXI") is True, "Debe aceptar 'XIXI' en validación de IXCM, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_icxm("CMC") is True, "Debe aceptar 'CMC' en validación de IXCM, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_icxm("DMD") is True, "Debe aceptar 'DMD' en validación de IXCM, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_icxm("IIX") is True, "Debe aceptar 'IIX' en validación de IXCM, pero no es romano válido (orden inválido)"
    assert validar_repeticiones_icxm("CCM") is True, "Debe aceptar 'CCM' en validación de IXCM, pero no es romano válido (orden inválido)"

