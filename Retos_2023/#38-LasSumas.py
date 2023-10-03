"""
/*
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)
 */
"""
import itertools

#Comprensión de listas
def sum_multiple(numbers:list, target:int):

  result = [seq for i in range(len(numbers), 0, -1)
            for seq in itertools.combinations(numbers, i)
            if sum(seq) == target]

  resultado = list(set(result))
  print(resultado)
  
def main():
   
  sum_multiple([1, 5, 3, 2],6)
  sum_multiple([1, 2, 3, 7, 7, 9, 10],10)
 
if __name__ == "__main__":
    main() 