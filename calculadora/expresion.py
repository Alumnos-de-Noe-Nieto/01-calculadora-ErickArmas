"""
Nivel 8: Orquestación del Pipeline Completo
Este módulo contiene la función principal para evaluar expresiones aritméticas de números romanos.
"""

from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    """
    Pipeline completo - Orquestación de todos los niveles.
    """
    
    # --- PASO 1: Parsing (Nivel 7) ---
    # 💡 PISTA PRIMERO: Llama a parsear_expresion(expresion) para obtener los tokens
    tokens = parsear_expresion(expresion)
    
    if not tokens:
        return 0

    # --- PASO 2: Limpieza ---
    # 💡 PISTA: Filtra tokens de tipo 'ESPACIO'
    tokens_utiles = [t for t in tokens if t.tipo != 'ESPACIO']

    # --- PASO 3: Evaluación (Nivel 8) ---
    # 💡 PISTA: Recorre los tokens restantes y aplica las operaciones correspondientes
    
    # Inicializamos el resultado con el primer número romano convertido
    # Al llamar a romano_a_entero, se disparan automáticamente las validaciones Niveles 1-6
    resultado = romano_a_entero(tokens_utiles[0].valor)
    
    # Recorremos el resto de la lista de dos en dos: [Operador, Número]
    i = 1
    while i < len(tokens_utiles):
        operador = tokens_utiles[i]
        proximo_numero = tokens_utiles[i + 1]
        
        # Convertimos el siguiente componente romano a entero
        valor_num = romano_a_entero(proximo_numero.valor)
        
        # Aplicamos la operación según el tipo de token
        if operador.tipo == 'SUMA':
            resultado += valor_num
        elif operador.tipo == 'RESTA':
            resultado -= valor_num
            
        i += 2

    # --- PASO 4: Validación Final ---
    # 💡 PISTA: Al final, valida que el resultado sea positivo (> 0)
    # 💡 PISTA: Si el resultado es <= 0, lanza ExpresionInvalida con mensaje descriptivo
    if resultado <= 0:
        raise ExpresionInvalida(
            f"Resultado inválido: {resultado}. "
            "Las expresiones romanas deben dar como resultado un número mayor a cero."
        )

    return resultado