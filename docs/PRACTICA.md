# Especificación de la Práctica - Calculadora Romana

Este documento contiene la especificación completa de la práctica Unidad 1: Calculadora de Números Romanos.

---

## 🎯 Descripción General

El objetivo de esta práctica es construir una **calculadora de números romanos** que simula un **pipeline de compilación**. Cada nivel de la práctica corresponde a una fase de un compilador real:

⚠️ **IMPORTANTE - Archivos Modificables:**

Solo puedes modificar los archivos dentro del directorio `calculadora/`. Cualquier intento de modificar archivos fuera de este directorio (como `tests/`, `docs/`, `.github/`, etc.) será **rechazado automáticamente** por GitHub al hacer push. Esto garantiza que la evaluación sea consistente para todos los estudiantes.

**Archivos que puedes modificar:**
- `calculadora/validaciones/alfabeto.py` (Nivel 1)
- `calculadora/validaciones/repeticiones_icxm.py` (Nivel 2)
- `calculadora/validaciones/repeticiones_vld.py` (Nivel 3)
- `calculadora/validaciones/orden_descendente.py` (Nivel 4)
- `calculadora/validaciones/restas.py` (Nivel 5)
- `calculadora/conversor.py` (Nivel 6)
- `calculadora/parser.py` (Nivel 7)
- `calculadora/expresion.py` (Nivel 8)

1. **Análisis Léxico:** Validar que los caracteres pertenecen al alfabeto válido
2. **Análisis Sintáctico:** Validar que la estructura siga las reglas gramaticales
3. **Análisis Semántico:** Validar que el significado sea correcto
4. **Generación de Código:** Transformar el lenguaje de entrada a otra representación
5. **Parsing:** Tokenizar y analizar estructuras complejas
6. **Orquestación:** Integrar todas las fases en un pipeline completo

Al completar la práctica, tendrás una calculadora que puede evaluar expresiones aritméticas como:

```
XIV + LX → 74
X - V → 5
MMMCMXCIX + I → 4000
```

---

## 📊 Pipeline de Compilación

| Fase de Compilador | Nivel Práctica | Archivo | Función a Implementar |
|-------------------|-----------------|----------|---------------------|
| Análisis Léxico - Alfabeto | Nivel 1 | `validaciones/alfabeto.py` | `validar_simbolos(cadena)` |
| Análisis Sintáctico I - Repeticiones I/X/C/M | Nivel 2 | `validaciones/repeticiones_icxm.py` | `validar_repeticiones_icxm(cadena)` |
| Análisis Sintáctico II - Repeticiones V/L/D | Nivel 3 | `validaciones/repeticiones_vld.py` | `validar_repeticiones_vld(cadena)` |
| Análisis Sintáctico III - Orden Descendente | Nivel 4 | `validaciones/orden_descendente.py` | `validar_orden_descendente(cadena)` |
| Análisis Semántico - Restas Válidas | Nivel 5 | `validaciones/restas.py` | `validar_restas(cadena)` |
| Generación de Código - Conversión | Nivel 6 | `conversor.py` | `romano_a_entero(cadena)` |
| Parsing - Expresiones | Nivel 7 | `parser.py` | `evaluar_expresion()`, `tokenizar_expresion()`, `validar_estructura_tokens()` |
| Orquestación - Pipeline | Nivel 8 | `expresion.py` | `evaluar(expresion)` |

---

## 🔧 Especificación por Nivel

---

### Nivel 1: Análisis Léxico - Alfabeto

**Archivo:** `calculadora/validaciones/alfabeto.py`

**Función:** `validar_simbolos(cadena: str) -> bool`

**Descripción:**
Validar que todos los caracteres de la cadena pertenezcan al alfabeto romano Σ = {I, V, X, L, C, D, M}.

**Requisitos:**
- Retornar `True` si todos los caracteres son válidos
- Retornar `False` si algún carácter no pertenece al alfabeto
- Retornar `False` si la cadena está vacía
- Ignorar espacios en blanco al inicio y final (usar `.strip()`)

**Pistas de implementación:**
- Usa `set()` para verificar pertenencia al alfabeto
- Usa `.strip()` para eliminar espacios laterales
- Usa `cadena.strip()` != "" para verificar que no esté vacía
- Puedes usar `set(cadena).issubset("IVXLCDM")`

**Casos de prueba:**
- `"XIV"` → `True`
- `"MCMXCIV"` → `True`
- `"ABCD"` → `False`
- `"X-IV"` → `False`
- `""` → `False`
- `"  XIV  "` → `True`

---

### Nivel 2: Análisis Sintáctico I - Repeticiones I/X/C/M

**Archivo:** `calculadora/validaciones/repeticiones_icxm.py`

**Función:** `validar_repeticiones_icxm(cadena: str) -> bool`

**Descripción:**
Validar que los símbolos I, X, C y M no se repitan más de 3 veces consecutivas.

**Requisitos:**
- Retornar `True` si I, X, C, M se repiten máximo 3 veces
- Retornar `False` si alguno de estos símbolos se repite 4 o más veces
- La cadena ya fue validada en Nivel 1 (solo símbolos válidos)

**Pistas de implementación:**
- Verifica si existen los patrones "IIII", "XXXX", "CCCC", "MMMM"
- Usa el operador `in` para buscar estos patrones en la cadena
- Usa la constante `SIMBOLOS_REPETIBLES` que contiene {'I', 'X', 'C', 'M'}
- Usa la constante `MAX_REPETICIONES = 3`

**Casos de prueba:**
- `"III"` → `True`
- `"IIII"` → `False`
- `"XXXX"` → `False`
- `"XIX"` → `True`
- `"MMMCMXCIV"` → `True`
- `"MMMM"` → `False`

---

### Nivel 3: Análisis Sintáctico II - Repeticiones V/L/D

**Archivo:** `calculadora/validaciones/repeticiones_vld.py`

**Función:** `validar_repeticiones_vld(cadena: str) -> bool`

**Descripción:**
Validar que los símbolos V, L y D no se repitan (máximo 1 vez).

**Requisitos:**
- Retornar `True` si V, L, D no se repiten
- Retornar `False` si alguno de estos símbolos se repite 2 o más veces
- La cadena ya fue validada en Niveles 1-2

**Pistas de implementación:**
- Verifica si existen los patrones "VV", "LL", "DD"
- Usa el operador `in` para buscar estos patrones en la cadena
- Usa la constante `SIMBOLOS_UNICOS` que contiene {'V', 'L', 'D'}
- Usa la constante `MAX_REPETICIONES = 1`

**Casos de prueba:**
- `"V"` → `True`
- `"VV"` → `False`
- `"LL"` → `False`
- `"MCMXCIV"` → `True`
- `"DD"` → `False`

---

### Nivel 4: Análisis Sintáctico III - Orden Descendente

**Archivo:** `calculadora/validaciones/orden_descendente.py`

**Función:** `validar_orden_descendente(cadena: str) -> bool`

**Descripción:**
Validar que los símbolos estén en orden descendente de valor (izquierda a derecha), excepto por las 6 formas sustractivas válidas.

**Requisitos:**
- Retornar `True` si el orden es descendente
- Retornar `False` si el orden no es descendente
- Permitir las 6 sustracciones válidas: IV, IX, XL, XC, CD, CM
- La cadena ya fue validada en Niveles 1-3

**Pistas de implementación:**
- Usa la constante `VALORES` con el valor de cada símbolo
- Usa la constante `SUSTRACCIONES_VALIDAS` con {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
- Recorre la cadena con un índice `i`
- Si `cadena[i:i+2]` es una sustracción válida, verifica que no haya múltiples repeticiones antes
- Si no es sustracción, verifica que el valor actual sea >= al siguiente
- Verifica que después de una sustracción, el orden descendente continúe

**Casos de prueba:**
- `"XVI"` → `True` (X > V > I)
- `"IVX"` → `False` (V es menor que X después de sustracción)
- `"MCMXCIV"` → `True` (varias sustracciones válidas)
- `"IIV"` → `False` (I repetido antes de IV)
- `"VIV"` → `False`

---

### Nivel 5: Análisis Semántico - Restas Válidas

**Archivo:** `calculadora/validaciones/restas.py`

**Función:** `validar_restas(cadena: str) -> bool`

**Descripción:**
Validar que las restas (sustracciones) sean válidas. Solo 6 pares específicos son permitidos.

**Requisitos:**
- Retornar `True` si todas las restas son válidas
- Retornar `False` si existe una resta inválida
- Solo permitir: IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)
- La cadena ya fue validada en Niveles 1-4

**Pistas de implementación:**
- Detecta una sustracción cuando el valor actual < valor siguiente
- Usa `VALORES[simbolo]` para obtener el valor numérico
- Verifica que el par `cadena[i:i+2]` esté en `SUSTRACCIONES_VALIDAS`
- Verifica que no haya múltiples repeticiones antes de la sustracción (ej: IIX es inválido)
- Recorre la cadena con un índice, avanza de 1 o 2 posiciones según corresponda

**Casos de prueba:**
- `"IV"` → `True`
- `"IX"` → `True`
- `"IL"` → `False` (49 no es una resta válida)
- `"IC"` → `False` (99 no es una resta válida)
- `"XIV"` → `True` (X + IV, IV es válida)
- `"IIX"` → `False` (II antes de IX)

---

### Nivel 6: Generación de Código - Conversión

**Archivo:** `calculadora/conversor.py`

**Función:** `romano_a_entero(cadena: str) -> int`

**Descripción:**
Convertir un número romano válido a su valor entero correspondiente (1-3999).

**Requisitos:**
- Retornar el valor entero del número romano
- La cadena ya fue validada en Niveles 1-5
- Lanzar `ExpresionInvalida` si la cadena no pasa validaciones

**Pistas de implementación:**
- Primero llama a todas las funciones de validación (Niveles 1-5)
- Si alguna validación falla, lanza `ExpresionInvalida` con mensaje descriptivo
- Usa un diccionario con los valores: `{'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}`
- **ALGORITMO RECOMENDADO:** Recorre de DERECHA a IZQUIERDA (reversed):
  - Mantén una variable `valor_previo` inicializada en 0
  - Si el valor actual < valor_previo → RESTAR (sustracción)
  - Si el valor actual >= valor_previo → SUMAR
  - Actualiza `valor_previo` con el valor actual
- Ejemplo: "IV" → recorres "V"(5) luego "I"(1) → I < V → 5 - 1 = 4
- Ejemplo: "VI" → recorres "I"(1) luego "V"(5) → V >= I → 1 + 5 = 6

**Casos de prueba:**
- `"I"` → `1`
- `"V"` → `5`
- `"IV"` → `4`
- `"IX"` → `9`
- `"XIV"` → `14`
- `"MCMXCIV"` → `1994`
- `"MMMCMXCIX"` → `3999`

---

### Nivel 7: Parsing - Expresiones

**Archivo:** `calculadora/parser.py`

**Funciones a implementar:**

#### Nivel 7.1: `evaluar_expresion(expresion: str) -> list[Token]`

**Descripción:**
Tokenizar y validar una expresión aritmética de números romanos.

**Requisitos:**
- Retornar lista de tokens si la expresión es válida
- Retornar lista vacía si la expresión está vacía
- Lanzar `ExpresionInvalida` si hay caracteres inválidos o estructura inválida

**Pistas de implementación:**
- Llama a `tokenizar_expresion(expresion)` para obtener los tokens
- Llama a `validar_estructura_tokens(tokens)` para validar la estructura
- Si la validación falla, lanza `ExpresionInvalida` con mensaje descriptivo

---

#### Nivel 7.2: `tokenizar_expresion(expresion: str) -> list[Token]`

**Descripción:**
Convierte una expresión de texto en una lista de tokens.

**Requisitos:**
- La expresión puede contener: números romanos, operadores (+, -), espacios
- Crear objetos `Token` para cada elemento encontrado
- Lanzar `ExpresionInvalida` si hay caracteres inválidos

**Pistas de implementación:**
- Recorre la expresión caracter por caracter con un índice `i`
- Usa `if-elif` para identificar:
  - Espacio → `Token('ESPACIO', ' ', i)`
  - Suma (+) → `Token('SUMA', '+', i)`
  - Resta (-) → `Token('RESTA', '-', i)`
  - Número romano (una o más letras) → `Token('ROMANO', romano, inicio)`
- Para números romanos, avanza el índice hasta encontrar un no-romano
- Si el caracter no es ninguno de los anteriores, lanza `ExpresionInvalida`

**Casos de prueba:**
- `"XIV + LX"` → tokens con ROMANO, ESPACIO, SUMA, ESPACIO, ROMANO
- `"X+V"` → tokens con ROMANO, SUMA, ROMANO (sin espacios)
- `"ABC"` → lanza `ExpresionInvalida`

---

#### Nivel 7.3: `validar_estructura_tokens(tokens: list[Token]) -> bool`

**Descripción:**
Valida que la expresión tenga una estructura válida.

**Requisitos:**
- Debe comenzar y terminar con un número romano
- Los operadores (+, -) deben estar entre números romanos
- Solo se permite un operador entre números
- Retornar `True` si la estructura es válida, `False` en caso contrario

**Pistas de implementación:**
- Filtrar tokens de tipo 'ESPACIO' para facilitar la validación
- Verificar que hay al menos 3 tokens (ROMANO, OPERADOR, ROMANO)
- Verificar que el número de tokens sea impar (alternancia correcta)
- Verificar que el primer y último token sean ROMANO
- Verificar alternancia correcta: posiciones pares = ROMANO, posiciones impares = OPERADOR

**Casos de prueba:**
- `[ROMANO, SUMA, ROMANO]` → `True`
- `[ROMANO, ESPACIO, RESTA, ESPACIO, ROMANO]` → `True`
- `[SUMA, ROMANO]` → `False` (no puede comenzar con operador)
- `[ROMANO, SUMA]` → `False` (no puede terminar con operador)
- `[ROMANO, SUMA, ROMANO, RESTA, ROMANO]` → `False` (dos operadores seguidos)

---

### Nivel 8: Orquestación - Pipeline Completo

**Archivo:** `calculadora/expresion.py`

**Función:** `evaluar(expresion: str) -> int`

**Descripción:**
Integrar todos los niveles para evaluar expresiones aritméticas completas de números romanos.

**Requisitos:**
- Evaluar expresiones como "XIV + LX", "X - V", "MMMCMXCIX + I"
- Retornar el resultado entero de la expresión
- Lanzar `ExpresionInvalida` si hay errores o si el resultado es negativo

**Pistas de implementación:**
- Llama a `evaluar_expresion(expresion)` (del parser) para obtener tokens
- Filtra tokens de tipo 'ESPACIO'
- Convierte el primer número romano a entero usando `romano_a_entero()`
- Recorre los tokens restantes de 2 en 2 (operador, número):
  - Si el operador es 'SUMA', suma el valor del número
  - Si el operador es 'RESTA', resta el valor del número
- Valida que el resultado sea positivo (> 0)
- Si el resultado es <= 0, lanza `ExpresionInvalida` con mensaje descriptivo

**Casos de prueba:**
- `"XIV + LX"` → `74` (14 + 60 = 74)
- `"X - V"` → `5` (10 - 5 = 5)
- `"MMMCMXCIX + I"` → `4000` (3999 + 1 = 4000)
- `"V - X"` → lanza `ExpresionInvalida` (resultado negativo)

---

## 📝 Tipos de Datos Esperados

### Token (dataclass)

Estructura de datos definida en `parser.py`:

```python
@dataclass
class Token:
    """
    Representa un token en una expresión aritmética de números romanos.

    Attributes:
        tipo: El tipo de token ("ROMANO", "SUMA", "RESTA", "ESPACIO")
        valor: El valor del token (cadena)
        posicion: La posición del token en la expresión original
    """

    tipo: str      # "ROMANO", "SUMA", "RESTA", "ESPACIO"
    valor: str     # Valor del token (ej: "XIV", "+", "-", " ")
    posicion: int  # Posición en la expresión original (índice del primer caracter)
```

### Retornos de Funciones

| Nivel | Función | Tipo de Retorno | Descripción |
|-------|----------|------------------|-------------|
| Nivel 1 | `validar_simbolos()` | `bool` | `True` si válido, `False` si inválido |
| Nivel 2 | `validar_repeticiones_icxm()` | `bool` | `True` si válido, `False` si inválido |
| Nivel 3 | `validar_repeticiones_vld()` | `bool` | `True` si válido, `False` si inválido |
| Nivel 4 | `validar_orden_descendente()` | `bool` | `True` si válido, `False` si inválido |
| Nivel 5 | `validar_restas()` | `bool` | `True` si válido, `False` si inválido |
| Nivel 6 | `romano_a_entero()` | `int` | Valor entero del número romano (1-3999) |
| Nivel 7.1 | `evaluar_expresion()` | `list[Token]` | Lista de tokens o lista vacía |
| Nivel 7.2 | `tokenizar_expresion()` | `list[Token]` | Lista de tokens |
| Nivel 7.3 | `validar_estructura_tokens()` | `bool` | `True` si válida, `False` si inválida |
| Nivel 8 | `evaluar()` | `int` | Resultado de la expresión aritmética |

**Total: 10 funciones a implementar** (Nivel 7 contiene 3 funciones)

---

## 🎓 Conceptos Teóricos Relevantes

Para completar esta práctica, debes comprender:

### Alfabeto (Σ) y Lenguaje
- **Alfabeto:** Conjunto finito de símbolos válidos (ej: {I, V, X, L, C, D, M})
- **Lenguaje:** Conjunto de cadenas formadas por símbolos del alfabeto que cumplen reglas específicas

### Análisis Léxico
- **Objetivo:** Verificar que todos los caracteres pertenezcan al alfabeto válido
- **En compiladores:** Primera fase, separa el código fuente en tokens básicos

### Análisis Sintáctico
- **Objetivo:** Verificar que la estructura siga las reglas gramaticales
- **En compiladores:** Verifica que el código tenga la sintaxis correcta
- **Ejemplo:** Verificar que "XVI" está en orden descendente

### Análisis Semántico
- **Objetivo:** Verificar que el significado sea correcto
- **En compiladores:** Verifica que las operaciones sean válidas
- **Ejemplo:** Verificar que "IV" sea una resta válida (4), pero "IL" no (49 no es una resta válida)

### Tokenización y Parsing
- **Tokenización:** Convertir texto en tokens (unidades significativas)
- **Parsing:** Analizar la estructura de los tokens según reglas gramaticales
- **En compiladores:** Segunda fase, construye el árbol de sintaxis abstracta

### Pipeline de Compilación
- Secuencia ordenada de transformaciones desde código fuente hasta código ejecutable
- Cada fase depende de la anterior
- Si una fase falla, el proceso se detiene

---

## 📚 Referencias Adicionales

- **Teoría completa:** `docs/NOTAS_DE_CLASE.pdf` (material del profesor)
- **Guía de pruebas:** `docs/PRUEBAS.md`
- **Guía de ruff:** `docs/GUIA_RUFF.md`
- **Tests de referencia:** Carpeta `tests/`

---

## 🧪 Pruebas Manuales con el CLI

Además de las pruebas automáticas, puedes probar tu implementación manualmente usando el REPL interactivo:

### Ejecutar el CLI

```bash
python3 -m calculadora
```

### Ejemplos de Uso

```
🏛 > XIV + LX
Resultado: 74

🏛 > X - V
Resultado: 5

🏛 > MMMCMXCIX + I
Resultado: 4000

🏛 > salir
¡Gracias por usar la calculadora romana!
```

### Casos de Prueba Recomendados

- Sumas básicas: `X + V`, `XIV + LX`
- Restas básicas: `X - V`, `MCMXC - X`
- Números complejos: `MMMCMXCIX + I`
- Expresiones sin espacios: `X+V`, `XIV+LX`
- Múltiples operaciones: `X + V + I`

> **Nota:** El CLI es útil para pruebas manuales rápidas, pero las pruebas automáticas (`pytest`) son la forma oficial de verificar que tu implementación es correcta.

---

**Versión:** 1.1
**Fecha:** Marzo 2026
**Proyecto:** Unidad 1 - Lenguajes y Autómatas I
