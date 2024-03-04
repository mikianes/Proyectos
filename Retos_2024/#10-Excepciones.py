""" /*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */ """

# Ejercicio


""" def division(a, b):
    return a / b


print(division(1, 0))
 """
# Extra

print("EJERCICIO EXTRA")


class mi_error(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self) -> str:
        return "Error " + str(self.valor)


def division(a, b):
    return a / b


def calcular(x, y):
    try:
        z = division(x, y)
        if z >= 5:
            raise mi_error(5)
        print(f"El resultado es:{z}")
    except ZeroDivisionError:
        print("Division por cero")
    except TypeError:
        print("El valor no es un número")
    except mi_error as e:
        print(e)
    finally:
        print("La Ejecución ha finalizado")


calcular(1, 0)
calcular("p", 0)
calcular(10, 2)
calcular(10, 10)
