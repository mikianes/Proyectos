"""
/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
"""
from string import ascii_lowercase

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
               "l": 12, "m": 13, "n": 14, "ñ": 15, "o": 16, "p": 17, "q": 18, "r": 19, "s": 20, "t": 21, "u": 22,
               "v": 23, "w": 24, "x": 25, "y": 26, "z": 27}

dict = "abcdefghijklmnñopqrstuvwxyz"

dict_lower_case = ascii_lowercase


def game(word: str):

    points = 0
    word_game = list(word)
    for letter in word:
        # Usando "diccionario"
        # value = diccionario.get(letter)
        # points = points + value

        # Usando "dict"
        # value = dict.find(letter)
        # points = points + value + 1

        # Usando ascii_lowercase
        value = dict_lower_case.find(letter)
        points = points + value + 1

    print(f"La puntuación de la palabra es: {points}.")
    if points == 100:
        print("Has ganado")
    elif points > 100:
        print(f"Te has pasado: {points-100} puntos.")
    else:
        print(f"Has perdido, te has quedado a {100-points} puntos.")


def main():

    print("LA PALABRA DE LOS 100 PUNTOS")
    word_input = input("Introduce una palabra:")
    game(word_input.lower())


if __name__ == "__main__":
    main()
