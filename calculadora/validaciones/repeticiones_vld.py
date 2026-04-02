def validar_repeticiones_vld(cadena: str) -> bool:
    """
    Valida que los símbolos V, L y D no se repitan (máximo 1).
    """
    # SIM110: Versión simplificada para Ruff
    return all(simbolo not in cadena for simbolo in ["VV", "LL", "DD"])

# IMPORTANTE: Presiona ENTER aquí al final para dejar una línea vacía.
