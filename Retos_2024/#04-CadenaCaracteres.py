"""  
 *
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos (1. aba 2. Ababa 3. Abalaba 4. acá 5. acurruca)
 * - Anagramas  (Roma-Amor, Roma-Mora, Frase-Fresa, Cosa-Saco, Acto-Cota, Broca-Barco)
 * - Isogramas Un isograma (del griego isos, 'igual' y gramma, 'letra') es una palabra o frase en la que cada letra aparece el mismo número de veces
 * - (anna)
 * - Ejemplos ( https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%239%20-%20HETEROGRAMA%2C%20ISOGRAMA%20Y%20PANGRAMA%20%5BF%C3%A1cil%5D/python/mouredev.py)
 * - https://www.youtube.com/watch?v=hkWsjk0VG7c
 * """


def palindromo(word1: str):
    print("-----PALINDROMO-----")

    if word1.lower() == word1[::-1].lower():
        print(f"{word1} es un Palindromo")
    else:
        print(f"{word1} no es un Palindromo")


def anagrama(word1: str, word2: str):
    print("-----ANAGRAMA-----")

    if sorted(word1.lower()) == sorted(word2.lower()):
        print(f"{word1} y {word2} son Anagramas")
    else:
        print(f"{word1} y {word2} no son Anagramas")


def isograma(word1: str):
    print("-----ISOGRAMA-----")

    clean_word = word1.lower()
    letter_list = []

    for letter in clean_word:
        if letter.isalpha():
            if letter in letter_list:
                return False
            letter_list.append(letter)

    return True


palindromo("aba")
anagrama("roma", "amor")
# isograma("anna", "murcielago")
print(isograma("murcielago"))
