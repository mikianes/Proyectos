"""
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
 */
"""
import random

opciones = ["Piedra","Papel","Tijeras","Lagarto","Spock"]

combinacion = {"Tijeras":["Papel","Lagarto"],
           "Papel":["Piedra","Spock"],
           "Piedra":["Lagarto","Tijeras"],
           "Lagarto":["Spock","Papel"],
           "Spock":["Tijeras","Piedra"]}

#Reglas del juego
def piedra():
    print("REGLAS")
    print("Tijeras cortan Papel")
    print("Papel tapa a Piedra")
    print("Piedra aplasta a Lagarto")
    print("Lagarto envenena a Spock")
    print("Spock rompe Tijeras")
    print("Tijeras decapitan Lagarto")
    print("Lagarto devora Papel")
    print("Papel desautoriza Spock")
    print("Spock vaporiza Piedra")
    print("Piedra aplasta Tijeras")
    input("Pulsa una tecla para continuar...")
 
 
# Elección random de opciones
def aleatorio ():
    
    eleccion = random.choice(opciones)
    return eleccion

# Comprobación opciones
def comprobacion(opcion):
    resultado = opcion in opciones
    return resultado
 
# Cálculo del Ganador   
def juego(reglas,jugadores):
    ronda = 0
    jugador1 = 0
    jugador2 = 0
    # Si quieremos ver las reglas llamamos a la función
    if reglas == "S":
        piedra()
    
    while ronda < 4:
        if jugadores == 1:
            uno = input("Elige entre Piedra, Papel, Tijeras, Largarto o Spock:")
            dos = aleatorio()
            comprobacionUno = comprobacion(uno)
            comprobacionDos = comprobacion(dos)
            if comprobacionUno == True and comprobacionDos == True:
                if uno == dos:
                    jugador1 += 1
                    jugador2 += 1
                elif dos in combinacion[uno]:
                    jugador1 += 1
                    ronda += 1
                else:
                    jugador2 += 1
                    ronda += 1
            else:
                print("Los datos no son correctos")
                main()
        elif jugadores == 2:
            uno = input("Elige entre Piedra, Papel, Tijeras, Largarto o Spock:")
            dos = input("Elige entre Piedra, Papel, Tijeras, Largarto o Spock:")
            comprobacionUno = comprobacion(uno)
            comprobacionDos = comprobacion(dos)
            if comprobacionUno == True and comprobacionDos == True:
                if uno == dos:
                    jugador1 += 1
                    jugador2 += 1
                elif dos in combinacion[uno]:
                    jugador1 += 1
                    ronda += 1
                else:
                    jugador2 += 1
                    ronda += 1
            else:
                print("Los datos no son correctos")
                main()
            
                
        print("Jugador 1:", uno, "Marcador:",jugador1, "-", "Jugador 2:", dos,"Marcador:", jugador2)
        
        if jugador1 == 2 or jugador2 == 2:
            ganador(jugador1, jugador2)
            break
        
               
# Notificación del Ganador
def ganador(jugador1, jugador2):
    
    if jugador1 == 2:
        print("El ganador es el Jugador1")
    elif jugador2 == 2:
        print("El ganador es el Jugador2")

def main():
    print("*****************************************")
    print("**Piedra, Papel, Tijera, Lagarto, Spock**")
    print("*****************************************")
    
    jugadores = ""
    reglas = ""
    
    #Control de opciones
    while True:
        try:
            reglas = str(input("¿Quieres ver las reglas del juego? (S/N)")).upper()
        except ValueError:
            print("Tienes que elegir entre S y N")
        
        if not reglas:
            print("Debes elegir entre S y N")
            continue
        if reglas != "S" and reglas != "N":
            print("Debes elegir entre S y N")
            continue
        else:
            break
    
    while True:
        try:
            jugadores = int(input("Elige entre 1 u 2 jugadores:"))
        except ValueError:
            print("Tienes que elegir un número")
        
        if not jugadores:
            print("Debes elegir entre 1 u 2 jugadores")
            continue
        if jugadores < 1 or jugadores > 2:
            print("Debes elegir entre 1 u 2 jugadores")
            continue
        else:
            break
    
    juego(reglas,jugadores)
   
 
if __name__ == "__main__":
    main()   