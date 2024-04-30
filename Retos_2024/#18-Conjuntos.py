"""
/*
* EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones(debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA(opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */
"""
ejercicio = [4, 6, 5, 1, 9]
print(f"Lista inicial:{ejercicio}")

# Ejercicio
print("-----EJERCICIO-----")
# Elemento al final
ejercicio.append(10)
print(f"Elemento añadido al final (10): {ejercicio}")
# Elemento al inicio
ejercicio.insert(0, 0)
print(f"Elemento añadido al inicio (0): {ejercicio}")
# Añade varios elementos en bloque al final
ejercicio.extend([11, 12])
print(f"Añade elementos en bloque al final [11,12]: {ejercicio}")
# Añade varios elementos en bloque a una posicion concreta
ejercicio[2:2] = [100, 200]
print(
    f"Añade varios elementos en  una posicion concreta [100,200]:{ejercicio}")
# Elimina un elemento en una posición concreta
ejercicio.pop(0)
print(f"Elimina un elemento en una posición concreta (0):{ejercicio}")
# Actualiza el valor de un elemento en una posición concreta
ejercicio[0] = 0
print(
    f"Actualiza el valor de un elemento en una posición concreta ( 4 a 0):{ejercicio}")
# Comprueba si un elemento está en un conjunto
if 100 in ejercicio:
    print("El elemento 100 está en la lista")
# Elimina todo el contenido del conjunto
ejercicio.clear()
print(f"Elimina todo el contenido: {ejercicio}")

# EJERCICIO EXTRA
print("-----EJERCICIO EXTRA-----")
conjunto1 = {1, 3, 5, 7, 9, 10}
conjunto2 = {2, 4, 6, 8, 10}
print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")

# Unión
print(f"Unión: {conjunto1.union(conjunto2)}")

# Intersección
print(f"Intersacción: {conjunto1.intersection(conjunto2)}")

# Diferencia
print(f"Diferencia en 1 y no en 2: {conjunto1.difference(conjunto2)}")

# Diferencia simétrica
print(f"Diferencia Simétrica: {conjunto1.symmetric_difference(conjunto2)}")
