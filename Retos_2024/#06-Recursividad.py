""" /*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */ """


def countdown(n: int):
    if n == 0:
        print(0)
    else:
        print(n)
        countdown(n-1)


def factorial(n: int):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


countdown(5)
print(factorial(5))
print(fibonacci(7))
print(fibonacci(10))
