"""
/*
 * Crea un juego interactivo por terminal en el que tendrás que adivinar 
 * el resultado de diferentes
 * operaciones matemáticas aleatorias (suma, resta, multiplicación 
 * o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 *   ...
 */
"""

import numpy as np
import random as rand
import time
from inputimeout import inputimeout 

suma = "+"
resta = "-"
multiplicacion = "*"
division = "/"


def calc(numNum:int,numNum1:int,orden:int):
    
    countdown = 3
    start_time = time.time()

    resultado = []
    resultado.append(rand.randrange(0,numNum+1))
    resultado.append(np.random.choice([suma, resta, multiplicacion ,division]))
    resultado.append(rand.randrange(1,numNum1+1))

    if resultado[1] == "+":
        resultado.append( resultado[0] +  resultado[2])
    elif  resultado[1] == "-":
        resultado.append( resultado[0] - resultado[2])
    elif  resultado[1] == "*":
        resultado.append( resultado[0] *  resultado[2])
    else:
        resultado.append( resultado[0] /  resultado[2])    
    
    print(f"Pregunta: {orden} , Operación: {resultado[0]} {resultado[1]} {resultado[2]} ({round(resultado[3],2)})") 
   
    try:
        time_over = inputimeout(prompt='¿Cual es el resultado de la operación?', timeout=10) 
    except Exception: 
        time_over = 'Se acabó el tiempo!'
        print(time_over) 
  
    result = time_over 
    if str(result) == str(round(resultado[3],2)):
        return "1"    
    else:
        return "2"
            
                   
def game():
    
    operations = 1
    aciertos = 0
   
    while operations < 21:
        
        if operations >= 1 and operations <= 5:  
            operacion = calc(9,9,operations)         
            
            if operacion == "1":
                print("Correcto")
                aciertos += 1
            else:
                print("Has fallado")
                break
             
        elif operations >= 6 and operations <=10:
            operacion = calc(99,9,operations)         
            
            if operacion == "1":
                print("Correcto")
                aciertos += 1
            else:
                print("Has fallado")
                break
            
        elif operations >= 11 and operations <=15:
            operacion = calc(99,99,operations)         
            
            if operacion == "1":
                print("Correcto")
                aciertos += 1
            else:
                print("Has fallado")
                break
        else:
            operacion = calc(999,99,operations)         
            
            if operacion == "1":
                print("Correcto")
                aciertos += 1
            else:
                print("Has fallado")
                break

        operations += 1
    
    print(f"Aciertos:{aciertos}")

def main():
    game()
        
if __name__ == "__main__":
    main() 