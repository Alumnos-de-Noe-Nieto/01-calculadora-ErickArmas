def validar_alfabeto(cadena: str) -> bool:
    """
    Valida que la cadena contenga únicamente símbolos del alfabeto romano.
    """
    # 1. Quitamos espacios de los lados
    cadena_limpia = cadena.strip()

    # 2. Si quedó vacía, no es válida
    if not cadena_limpia:
        return False

    # 3. Definimos los símbolos permitidos
    alfabeto = "IVXLCDM"

    # 4. Revisamos que cada letra de la cadena esté en el alfabeto
    # Usamos all() para cumplir con la sugerencia SIM110 de Ruff
    return all(letra in alfabeto for letra in cadena_limpia)
