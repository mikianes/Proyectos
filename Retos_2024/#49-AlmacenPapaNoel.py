""" /*
* EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y
 *   el programa le indicará para cada uno lo siguiente:
 * - Correcto: Si el caracter está en la posición correcta.
 * - Presente: Si el caracter existe, pero esa no es su posición.
 * - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 *
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
 */ """

import random
import numpy as np

keys = ["A", "B", "C", "1", "2", "3"]
success = 0


def game(santa_list: list, password: list):
    global success
    success = 0
    for i in range(4):
        if santa_list[i] == password[i]:
            print(f"{santa_list[i]} :Correcto")
            success += 1
        elif santa_list[i] in password:
            print(f"{santa_list[i]} :Presente")
        else:
            print(f"{santa_list[i]} :Incorrecto")

    if success == 4:
        print("La puerta del almacén se abre")
        exit()


def comprobation(key: list, password: list) -> bool:

    counter = 0
    for value_password in password:
        if value_password in key:
            counter += 1

    if counter == 4 and len(password) == 4:
        return True
    else:
        return False


def main():

    print("Santa ha perdido la clave del almacen de regalos, ayudale a recordar")
    password = np.random.choice(keys, 4, replace=False)
    print(password)

    for i in range(5):
        print(f"Intentos restantes:{5-i}")
        santa_password = input(
            "Introduce la contraseña. 4 caracteres:números (1, 2 o 3) o letras (A,B o C)): ")
        santa_pasword_list = list(santa_password.upper())

        z = comprobation(keys, santa_pasword_list)
        if z != True:
            print("No cumple con las características")
        else:
            game(santa_pasword_list, password)

    if i == 4 and success < 4:
        print("Santa este año no podrá repartir los regalos")


if __name__ == "__main__":
    main()
