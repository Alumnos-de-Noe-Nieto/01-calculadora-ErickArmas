from calculadora.validaciones.alfabeto import validar_simbolos


def test_nivel_1_1_el_vacio_de_cartago():
    """Prueba 1.1: Validar que una cadena vacía es rechazada."""
    assert validar_simbolos('') is False, (
        'Una cadena vacía no es un numero romano válido'
    )


def test_nivel_1_2_la_invasion_barbara():
    """Prueba 1.2: Validar que caracteres latinos arrojaran error."""
    invalidos = ['A', 'B', '1', '123', 'hola', 'XIVP']
    for caso in invalidos:
        assert validar_simbolos(caso) is False, (
            f"Debe rechazar caracteres inválidos como '{caso}'"
        )


def test_nivel_1_3_espias_entre_nosotros():
    """Prueba 1.3: Rechazar cadenas que combinan símbolos válidos con inválidos."""
    assert validar_simbolos('X-IV') is False, (
        "Debe rechazar cadenas con guiones como 'X-IV'"
    )
    assert validar_simbolos('MCM P') is False, (
        "Debe rechazar cadenas con espacios como 'MCM P'"
    )


def test_nivel_1_4_el_legionario_solitario():
    """Prueba 1.4: Validar cadenas de un solo símbolo."""
    assert validar_simbolos('I') is True, "Debe aceptar el símbolo 'I'"
    assert validar_simbolos('V') is True, "Debe aceptar el símbolo 'V'"
    assert validar_simbolos('X') is True, "Debe aceptar el símbolo 'X'"
    assert validar_simbolos('L') is True, "Debe aceptar el símbolo 'L'"
    assert validar_simbolos('C') is True, "Debe aceptar el símbolo 'C'"
    assert validar_simbolos('D') is True, "Debe aceptar el símbolo 'D'"
    assert validar_simbolos('M') is True, "Debe aceptar el símbolo 'M'"


def test_nivel_1_5_el_triunfo_del_cesar():
    """Prueba 1.5: Validar que una cadena completa sea aceptada."""
    assert validar_simbolos('XIV') is True, (
        "Debe aceptar números romanos válidos como 'XIV'"
    )
    assert validar_simbolos('MCMXCIV') is True, (
        "Debe aceptar números romanos válidos como 'MCMXCIV'"
    )


def test_nivel_1_6_la_venganza_de_minerva():
    """
    Prueba 1.6: Nivel Pesadilla.
    Casos ultra-rebuscados que incluyen Unicode, Bidi y caracteres invisibles.
    """
    assert validar_simbolos('Ⅹ') is False, (
        "Cuidado: 'Ⅹ' (U+2169) es un símbolo Unicode, no la letra latina 'X'"
    )
    assert validar_simbolos('Ι') is False, (
        "Cuidado: 'Ι' (U+0399) es Iota griega, no la letra latina 'I'"
    )
    assert validar_simbolos('\u202eVI\u202c') is False, (
        'Debe rechazar caracteres de control de dirección (Bidi Override)'
    )
    assert validar_simbolos('I\u200bX') is False, (
        'Debe rechazar espacios de ancho cero (Zero-width space)'
    )
    assert validar_simbolos('X\tI\nV') is False, (
        'Debe rechazar tabs o saltos de línea internos'
    )
    assert validar_simbolos('X\x08V') is False, (
        'Debe rechazar caracteres de control como Backspace (\\x08)'
    )
    assert validar_simbolos('XIV\0') is False, 'Debe rechazar el carácter nulo (\\0)'
    assert validar_simbolos('IV\x1a') is False, (
        'Debe rechazar caracteres de control ASCII (\\x1a)'
    )
    assert validar_simbolos('\ufeffXIV') is False, (
        'Debe rechazar el Byte Order Mark (BOM)'
    )


def test_falsos_positivos():
    """
    Los siguientes numeros pasan la validacion de simbolos, pero no son numeros romanos validos aun.
    """
    # Falsos positivos: pasan validación de símbolos pero no son romanos válidos
    assert validar_simbolos('IIII') is True, (
        "Debe aceptar 'IIII' en validación de símbolos, pero no es romano válido (demasiadas I)"
    )
    assert validar_simbolos('VV') is True, (
        "Debe aceptar 'VV' en validación de símbolos, pero no es romano válido (dos V)"
    )
    assert validar_simbolos('XXXX') is True, (
        "Debe aceptar 'XXXX' en validación de símbolos, pero no es romano válido (demasiadas X)"
    )
    assert validar_simbolos('LL') is True, (
        "Debe aceptar 'LL' en validación de símbolos, pero no es romano válido (dos L)"
    )
    assert validar_simbolos('CCCC') is True, (
        "Debe aceptar 'CCCC' en validación de símbolos, pero no es romano válido (demasiadas C)"
    )
    assert validar_simbolos('DDDD') is True, (
        "Debe aceptar 'DDDD' en validación de símbolos, pero no es romano válido (demasiadas D)"
    )
    assert validar_simbolos('MMMM') is True, (
        "Debe aceptar 'MMMM' en validación de símbolos, pero no es romano válido (demasiadas M)"
    )
    assert validar_simbolos('IIV') is True, (
        "Debe aceptar 'IIV' en validación de símbolos, pero no es romano válido (orden inválido)"
    )
    assert validar_simbolos('VIX') is True, (
        "Debe aceptar 'VIX' en validación de símbolos, pero no es romano válido (orden inválido)"
    )
    assert validar_simbolos('IXC') is True, (
        "Debe aceptar 'IXC' en validación de símbolos, pero no es romano válido (orden inválido)"
    )
    assert validar_simbolos('MCMD') is True, (
        "Debe aceptar 'MCMD' en validación de símbolos, pero no es romano válido (orden inválido)"
    )
