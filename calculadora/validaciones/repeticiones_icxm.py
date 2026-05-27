def validar_repeticiones_icxm(cadena: str) -> bool:
    """
    Valida que los símbolos I, X, C, M no se repitan más de 3 veces consecutivas.
    """
    patrones_invalidos = ["IIII", "XXXX", "CCCC", "MMMM"]

    # SIM110: Usamos una expresión generadora con all() para mayor eficiencia
    return all(patron not in cadena for patron in patrones_invalidos)


