"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""
import random


def generador(longitud, mayuscula, numero, simbolo):
    print("Entro a Generador")
    list_minus = ("a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z")
    list_mayus = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    list_nums = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    list_simbolos = ("!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "^", "_", "`", "{", "|", "}", "~")

    password = ""
    lista = ""
    lista = list_minus
    
    if mayuscula == "S":
        lista += list_mayus
    if numero == "S":
        lista += list_nums
    if simbolo == "S":
        lista += list_simbolos

    for i in range(longitud):
        password += random.choice(lista)
                
    print("La contraseña es: ", password)    
        
def datos():
    
    #Introducción de parámetros
    esNumero = ""
    maymin = ""
    numeros = ""
    simbolos = ""
        
    while True:
        try:
            esNumero = int(input("Elige una longitud entre 8 y 16 caracteres:"))
        except ValueError:
            print("Tienes que elegir un número")
        
        if not esNumero:
            print("Debes elegir una longitud entre 8 y 16")
            continue
        if esNumero < 8 or esNumero > 16:
            print("Debes elegir una longitud entre 8 y 16")
            continue
        else:
            break
        
    while True:
        try:
            maymin = str(input("¿Quieres usar letras mayúsculas? S/N:")).upper()
        except ValueError:
            print("Tienes que elegir S/N")
        
        if not maymin:
            print("Tienes que elegir S/N")
            continue
        if maymin != "S" and maymin != "N":
            print("Tienes que elegir S/N")
            continue
        else:
            break
    
    while True:
        try:
            numeros = str(input("¿Quieres usar números? S/N:")).upper()
        except ValueError:
            print("Tienes que elegir S/N")
        
        if not numeros:
            print("Tienes que elegir S/N")
            continue
        if numeros != "S" and numeros != "N":
            print("Tienes que elegir S/N")
            continue
        else:
            break
    
    while True:
        try:
            simbolos = str(input("¿Quieres usar símbolos? S/N:")).upper()
        except ValueError:
            print("Tienes que elegir S/N")
        
        if not simbolos:
            print("Tienes que elegir S/N")
            continue
        if simbolos != "S" and simbolos != "N":
            print("Tienes que elegir S/N")
            continue
        else:
            break
        
    generador(esNumero,maymin,numeros,simbolos)



def main():
    print("**************************")
    print("**Generador de passwords**")
    print("**************************")
    datos()
 
if __name__ == "__main__":
    main()    