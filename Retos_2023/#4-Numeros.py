"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""
import array as arr 

def primo(primo):
    #Primo
    for n in range(2,primo):
        if primo % 2 == 0:
            #print(primo, "no es primo", n, "es divisor")
            return False
    return True

def par(par):
    if par % 2 == 0:
       return True
    else:
        return False

def fibonacci(fibo):
    n1 = 0
    n2 = 1
    resultado = []
    for y in range(1,fibo+1):
        if y == n1 + n2:
            resultado.append(y)
            n1 = n2
            n2 = y
    if fibo in resultado:
        return True
    else:
        return False

def numeros(num):
    cadena = "El número "
   
    primos = primo(num)
    pares = par(num)
    fibo = fibonacci(num)
    
    if primos == True:
        cadena = cadena + str(num) + " es primo,"
    else:
        cadena = cadena + str(num) + " no es primo,"
        
    if pares == True:
        cadena = cadena + " par y"
    else:
        cadena = cadena + " impar y"
        
    if fibo == True:
        cadena = cadena + " es fibonacci."
    else:
        cadena = cadena + " no es fibonacci."    
    
    print(cadena)



def main():
    print("*********************************")
    print("**Par, Impar, Primo y Fibonacci**")
    print("*********************************")
    numeros(7)
    numeros(2)
    numeros(13)
    numeros(4)
    
 
if __name__ == "__main__":
    main()   