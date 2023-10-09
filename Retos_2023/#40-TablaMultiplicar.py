"""
    /*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */
    
"""

def tabla(num:int):
    for a in range(1, 11): print(f"{num} x {a} = {num*a}")
            
def main():
   tabla(1)
    
if __name__ == "__main__":
    main() 