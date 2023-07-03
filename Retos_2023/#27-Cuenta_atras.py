"""
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
"""
import time

def cuenta_atras (number:int,sec:int):
    
    for i in reversed(range(1, number +1)):
        print(i)
        time.sleep(sec)
    
    print("FIN")
    exit()

def main():
    
    count = input("Introduce el número de inicio de la cuenta atrás:")
    seconds = input("Introduce los segundos entre cada cuenta:")
    
    cuenta_atras(int(count),int(seconds)) if str.isdigit(count) and str.isdigit(seconds) else print("Datos erróneos, vuelve a introducirlos"), main()
    
   
if __name__ == "__main__":
    main()  

