"""/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */"""
import random as rnd

#Función que dada la palabra, el caracter y el indice, sustituye la letra por el caracter
def cambio(palabra,caracter,index):
    return palabra[:index] + caracter + palabra[index+1:]
 
def random(a):
    return (rnd.randrange(0,a))

#Función que pinta los fallos
def fallos(numF):
    print("Entramos a fallos")
    if numF == 2:
        print("O")
        print("|")
    elif numF == 1:
        print(" O")
        print("/|\\")
    elif numF == 0:
        print(" O")
        print("/|\\")
        print("/\\")

def juego(listaT, listaO,correcta):
    
    intentos = 3
    
    while intentos > 0:
        
        if listaT == listaO:
            print("Enhorabuena has ganado")
            exit()
        
        txt = input ("Inserta una letra o la palabra adivinada:")
        texto = txt.lower()
        
        if texto == correcta.lower():
            print("Has ganado")
            exit()
        
        if len(texto) > 1:
            print("Debes introducir una letra o la palabra entera.")
            intentos -= 1
            fallos(intentos)
            print("Te quedan " + str(intentos) + " intentos.")
            if intentos == 0:
                print("Has perdido.")
                fallos(intentos)
        elif len(texto) == 1:
            #Comprobamos si la letra introducida existe en la palabra y corresponde una letra oculta.
            indexes = [i for i, j in enumerate(listaO) if j == texto] #Obtenemos los índices donde se encuentran las letras en la palabra original
            if len(indexes) < 1:
                intentos -= 1
                fallos(intentos)
                print("Fallaste, te quedan " + str(intentos) + " intentos.")
            elif len(indexes) > 0:
                for x in indexes:
                    if listaT[x] == listaO[x]: #En el caso de que se introduzca una letra y ya se encuentre resuelta.
                        intentos -= 1
                        fallos(intentos)
                        print("Fallaste, la letra ya estaba, te quedan " + str(intentos) + " intentos.")
                    else: #Sustituimos el caracter que se encuentra en la posicion x por la letra introducida.
                        listaT[x]=texto
                        print(listaT)
                        resultado = "".join(listaT)
                        print(resultado)
                    
        if intentos == 0:
            fallos(intentos)
            print("Has perdido")

#Función en la que hacemos el tratamiento de la palabra sustituyendo el 60% por el caracter _
def tratamiento(palabra):
    original = palabra
    tratada = original
    
    longitud = len(palabra)
    
    limit = (int(longitud) * 0.6)
    limite = round(limit)
    for indice in range(limite):
        indice = random(longitud)
        tratada = cambio(tratada,"_",indice)
        
    listatratada = list(tratada)
    listaoriginal= list(original)
    print(listatratada)
    print(listaoriginal)
    juego(listatratada,listaoriginal,original)
    

def main():
    palabra = input ("Introduce una palabra:")
    tratamiento(palabra.lower())
    
if __name__ == "__main__":
    main()  