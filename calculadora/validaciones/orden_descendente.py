def validar_orden_descendente(cadena: str) -> bool:
    """
    Valida que los símbolos estén en orden descendente de valor (izquierda a derecha).
    """
    # N806: Usamos minúsculas para variables locales según PEP 8
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    sustracciones_validas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    i = 0
    ultimo_valor_procesado = float('inf')

    while i < len(cadena):
        # Caso 1: Revisar si hay una sustracción de dos caracteres (ej: IV, IX)
        par_actual = cadena[i:i+2]

        if len(par_actual) == 2 and par_actual in sustracciones_validas:
            valor_sustraido = valores[par_actual[1]] - valores[par_actual[0]]

            # Regla: No puede haber un símbolo igual al que resta justo antes (ej: IIV)
            if i > 0 and cadena[i-1] == cadena[i]:
                return False

            # Regla: El valor total de la sustracción debe ser menor al anterior
            if valor_sustraido >= ultimo_valor_procesado:
                return False

            ultimo_valor_procesado = valor_sustraido
            i += 2  # Saltamos ambos caracteres
        else:
            # Caso 2: Símbolo individual
            valor_actual = valores[cadena[i]]

            # Regla: El valor debe ser menor o igual al anterior
            if valor_actual > ultimo_valor_procesado:
                return False

            ultimo_valor_procesado = valor_actual
            i += 1

    return True
