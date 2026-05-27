def validar_restas(cadena: str) -> bool:
    """
    Valida que las restas sigan las reglas oficiales del sistema romano.
    """
    # N806: Nombres en minúsculas para variables locales
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones_validas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    # 1. Bloqueamos repeticiones inválidas antes de una resta (IIV, XXL, etc.)
    # SIM110: Podríamos usar all(), pero para legibilidad con esta lista está bien
    restas_repetidas_invalidas = ["IIV", "IIX", "XXL", "XXC", "CCD", "CCM"]
    for patron in restas_repetidas_invalidas:
        if patron in cadena:
            return False

    # 2. Bloqueamos restas no permitidas (como IL, VX, IC)
    for i in range(len(cadena) - 1):
        actual = cadena[i]
        siguiente = cadena[i + 1]

        # SIM102: Combinamos los if en una sola línea con 'and'
        if valores[actual] < valores[siguiente] and (actual + siguiente) not in sustracciones_validas:
            return False

    return True
