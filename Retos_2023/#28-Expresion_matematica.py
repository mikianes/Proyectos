"""
/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */
"""

import re


def expression(expression:str):
    
    #x = re.findall(r"^[\d.]\s[-+*/()]\s[\d.]+$", expression)
    x = re.findall(r'^[\d\s+-/*\s()]+$',expression)
    
    
    if len(x) != 0:
        print(f"La expresión {expression} es correcta")
    else:
        print(f"La expresión {expression} es incorrecta")
    
def main():
    
   expression("4 + 3 + 9 * 7 / 3 * 5 + 5 * 9")
   expression("5 / 7 a 8 * 8")
   expression("r * 4")
   expression("4 a 6")
   expression("5 + -7")
    
   
if __name__ == "__main__":
    main()  