""" /*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */ """


# Ejercicio


def sum(num1: int, num2: int) -> int:
    print("Entro")

    return num1 + num2


print(sum(10, 3))

# Extra

names = {"name": "Pedro", "age": "41", "birth_date": "10/03/1983",
         "programming_languajes": ["Java", "Python", "SQL"]}
