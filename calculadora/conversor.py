"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos

# Diccionario auxiliar para la conversión de valores
VALORES_ROMANOS = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def romano_a_entero(cadena: str) -> int:
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.
    """
    
    # --- PASO 1: Validaciones (Niveles 1-5) ---
    # 💡 PISTA PRIMERO: Llama a todas las validaciones ANTES de convertir
    
    if not validar_simbolos(cadena):
        raise ExpresionInvalida(f'La cadena "{cadena}" contiene símbolos inválidos')

    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida(f'La cadena "{cadena}" tiene una repetición ilegal de I/X/C/M')

    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida(f'La cadena "{cadena}" tiene una repetición ilegal de V/L/D')

    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida(f'La cadena "{cadena}" tiene un orden incorrecto')

    if not validar_restas(cadena):
        raise ExpresionInvalida(f'La cadena "{cadena}" contiene restas inválidas')


    # --- PASO 2: Conversión (Nivel 6) ---
    # 💡 PISTA: Recorremos la cadena para calcular el valor total
    
    total = 0
    valor_anterior = 0
    
    # Recorremos de derecha a izquierda para aplicar la lógica de suma/resta fácilmente
    for caracter in reversed(cadena):
        valor_actual = VALORES_ROMANOS[caracter]
        
        # Si el valor actual es menor que el anterior (ej: IV -> el 1 es menor que el 5), se resta
        if valor_actual < valor_anterior:
            total -= valor_actual
        else:
            # Si es mayor o igual, se suma (ej: VI -> el 5 es mayor que el 1)
            total += valor_actual
            
        valor_anterior = valor_actual
        
    return total