"""
/*
 * Crea un programa que simule la competición de dos coches en una pista.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
 * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la meta.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la meta.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
 *   
 */
"""

import random as rand
import time

circuitA = []
circuitB = []

def randomObstacle(min:int,max:int):
    obstacules = 0
    obstacules = rand.randrange(min,max+1)
    return obstacules
    
def printCircuitsStatus(circuit:list):
    print(*circuit)
  

def race(circuitA:list,circuitB:list):
    crashA = False
    crashB = False
    crash = "💥"
    finishA = False
    finishB = False
    init_lenA = int(len(circuitA))
    init_lenB = int(len(circuitB))
    
    while finishA == False and finishB == False:
    # Code executed here
        #CircuitA
        ObstaclesA = randomObstacle(1,3)
        print(f"Avances A:{ObstaclesA}")
        rightA = init_lenA - ObstaclesA
        if crashA == False:
            if circuitA[0] == "🚙" or rightA < 0:
                circuitA[0] = "🚙"
                finishA = True
            else:
                try:
                    road = circuitA.index("🚙")
                    circuitA[road]="_"    
                except Exception: 
                    road = circuitA.index("💥")
                    circuitA[road]="💥" 
                if (circuitA[rightA-1]) == "🌲":
                    circuitA[rightA-1] = "💥"
                    crashA = True
                else: 
                    circuitA[rightA-1] = "🚙"
            init_lenA = init_lenA - ObstaclesA
        else:
            crashA = False
            
            
        #CircuitB
        ObstaclesB = randomObstacle(1,3)
        print(f"Avances B:{ObstaclesB}")
        rightB = init_lenB - ObstaclesB
        if crashB == False:
            if circuitB[0] == "🚗" or rightB < 0:
                circuitB[0] = "🚗"
                finishB = True
            else:
                try:
                    road = circuitB.index("🚗")
                    circuitB[road]="_"    
                except Exception: 
                    road = circuitB.index("💥")
                    circuitB[road]="💥" 
                if (circuitB[rightB-1]) == "🌲":
                    circuitB[rightB-1] = "💥"
                    crashB = True
                else: 
                    circuitB[rightB-1] = "🚗"
            init_lenB = init_lenB - ObstaclesB
        else:
            crashB = False
        

        
        print(*circuitA)
        print("----------------------")
        print(*circuitB)
        
        time.sleep(1)
    
    if(finishA == True and finishB == True):
        print("Empate")
    elif (finishA == True):
        print("Ganador: 🚙 ")
    else:
        print("Ganador: 🚗 ")

def inizialiceCircuits(lista:list,long:int,car:str)->list:
    
    lista = [ '_' for x in range(long+2)]
    longitud = len(lista)
    lista[0]= "🏁"                                   # Se añade bandera
    lista[longitud-1] = car                       # Se añade coche    
    obstaclesA = randomObstacle(1,3)                    # Se obtiene el número de obstaculos
    print(f"Obstaculos Circuito 1:{obstaclesA}")
    for i in range (1, obstaclesA+1):                   # Basandose en el número de obstáculos se obtiene su posición
        obstaculeA = randomObstacle(1,long)
        while lista[obstaculeA] == "🌲":             # Mientras exista el obstáculo en el array, se vuelve a generar una posición
            obstaculeA = randomObstacle(1,long)
        
        print(f"Posicion obstacule {i}:{obstaculeA}")
        lista[obstaculeA] = "🌲"                     # Se sustituye "_" por 🌲
    
    return lista
    
def main():  
    
    print("Carrera: 🏁🚗🚙🌲💥")
    longCircuits = input("Introduce la longitud del circuito:")
    global circuitA 
    global circuitB 
    carA = "🚙"
    carB = "🚗"
    circuitA = inizialiceCircuits(circuitA,int(longCircuits),carA)
    circuitB = inizialiceCircuits(circuitB,int(longCircuits),carB)
    print("__________________________")
    printCircuitsStatus(circuitA)
    printCircuitsStatus(circuitB)
    print("___________________________")
    race(circuitA,circuitB)
    
   
        
if __name__ == "__main__":
    main() 