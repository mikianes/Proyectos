"""/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
 """

import random as rnd

resultado1 = "love"
resultado2 = "love"

#Función de aleatorio entre 0 y 1
def random():
    return (rnd.randrange(1,3))
        
def game():
   
    global resultado2
    global resultado1
    resultado = random()
    
    match resultado:
        case 1:
            if resultado1 == "love":
                resultado1 = "15"
                   
            elif resultado1 == "15":
                resultado1 = "30"
                
            elif resultado1 == "30":
                if resultado2 == "40":
                    resultado2 = "Deuce"
                    resultado1 = "Deuce"
                else: 
                    resultado1 = "40"
            
            elif resultado1 == "40" and resultado2 != "40":
                resultado1 = "Ha ganado el P1"
                print("Ha ganado el P1", "Resultado:", resultado)
                exit()
            
            elif resultado1 == "Deuce" and resultado2 == "Deuce":
                resultado1 = "Ventaja P1"
            
            elif resultado1 == "Deuce" and resultado2 != "Deuce":
                 resultado2 = "Deuce"
                 resultado1 = "Deuce"
                
            elif resultado1 == "Ventaja P1" and resultado2 == "Ventaja P2":
                resultado1 = "Deuce"
                resultado2 = "Deuce"
            
            elif resultado1 == "Ventaja P1":
                resultado1 = "Ha ganado el P1"
                print("Ha ganado el P1" , "Resultado:", resultado)
                exit()
        case 2:
             if resultado2 == "love":
                resultado2 = "15"
               
             elif resultado2 == "15":
                resultado2 = "30"
                
             elif resultado2 == "30":
                  if resultado1 == "40":
                    resultado1 = "Deuce"
                    resultado2 = "Deuce"
                  else: 
                    resultado2 = "40"
                
             elif resultado2 == "40" and resultado1 != "40":
                resultado2 = "Ha ganado el P2"
                print("Ha ganado el P2" , "Resultado:", resultado)
                exit()
            
             elif resultado2 == "Deuce" and resultado1 == "Deuce":
                resultado2 = "Ventaja P2"
            
             elif resultado2 == "Deuce" and resultado1 != "Deuce":
                 resultado2 = "Deuce"
                 resultado1 = "Deuce"
            
             elif resultado2 == "Ventaja P2" and resultado1 == "Ventaja P1":
                resultado1 = "Deuce"
                resultado2 = "Deuce"
                
             elif resultado2 == "Ventaja P2":
                resultado2 = "Ha ganado el P2"
                print("Ha ganado el P2" , "Resultado:", resultado)
                exit()
       
    
    if resultado1 == "Deuce" and resultado2 == "Deuce":
        print ("Deuce", "Resultado:",resultado)
    elif resultado1 == "Ventaja P1":
        print ("Ventaja P1", "Resultado:", resultado)
    elif resultado1 == "Ventaja P2":
        print ("Ventaja P2", "Resultado:",resultado)
    else:
        print(resultado1, "-", resultado2, "Resultado:",resultado)
        
    game()
#Petición de nombres
def inicial():
    game()
    
#Llamada inicial
inicial()
 
 