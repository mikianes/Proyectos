""" /*
* EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA(opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
 */ """

# EXTRA

from abc import ABC, abstractmethod


class calculator(ABC):
    @abstractmethod
    def result(self):
        pass


class addition(calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def result(self):
        return self.num1 + self.num2


class subtraction(calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def result(self):
        return self.num1 - self.num2


class multiplication(calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def result(self):
        return self.num1 * self.num2


class division(calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def result(self):
        return self.num1 / self.num2


class power(calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def result(self):
        return self.num1 ** self.num2


calc = [addition(1, 1), subtraction(10, 5),
        multiplication(5, 5), division(5, 5), power(2, 3)]


for calculator in calc:
    print(calculator.result())
