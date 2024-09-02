""" /*
* EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */ """
import random as rnd


def random(number: int, race) -> int:
    try:
        return rnd.randrange(1, number)
    except ValueError:
        print(f"No quedan mas anillos para los {race}.")
        exit()
    except TypeError:
        print("No se puede realizar la operación")
        exit()


def par(par):
    if par % 2 == 0:
        return True
    else:
        return False


def primo(primo):
    # Primo
    for n in range(2, primo):
        if primo % 2 == 0:
            # print(primo, "no es primo", n, "es divisor")
            return False
    return True


def distributionOfRings(rings: int):
    # Con random y solo una solución
    """   print(rings)
      manufacturedRings = rings
      # Sauron
      print("Sauron: 1")
      rings = rings - 1

      # Elfos -> impar
      elvenNumber = ""
      while elvenNumber != False:
          elvenCount = random(rings, "Elfos")
          elvenNumber = par(elvenCount)
          if elvenNumber == False:
              rings = rings - elvenCount
              break
      print(f"Elfos: {elvenCount}")

      # Enanos -> primo
      gnomeNumber = ""
      while gnomeNumber != True:
          gnomeCount = random(rings, "Enanos")
          gnomeNumber = primo(gnomeCount)
          if gnomeNumber == True:
              rings = rings - gnomeCount
              break
      print(f"Gnomos: {gnomeCount}")

      # Hombres -> par
      humanNumber = ""
      while humanNumber != True:
          humanCount = random(rings, "Hombres")
          humanNumber = par(humanCount)
          if humanNumber == True:
              rings = rings - humanCount
              break
      print(f"Humanos: {humanCount}")

      # Se suma 1 por el anillo de Sauron
      totalRings = elvenCount + gnomeCount + humanCount + 1
      if totalRings < manufacturedRings:
          print(f"Gollum ha robado {manufacturedRings - totalRings} anillos.")
      else:
          print(f"Gollum se que quedado con las ganas") """

    # Buscando todas las combinaciones posibles. Recursividad.
    elves = [x for x in range(1, rings) if not par(x)]
    humans = [x for x in range(1, rings) if par(x)]
    gnomes = [x for x in range(1, rings) if primo(x)]

    # print(f"{elves},{humans},{gnomes}")

    combinacion = []

    for elfo in elves:
        anillos = elfo
        for enano in gnomes:
            anillos += enano
            for hombre in humans:
                anillos += hombre
                if anillos == rings - 1:
                    combinacion.append(
                        {"elfos": elfo, "enanos": enano, "hombres": hombre, "sauron": 1})
                anillos -= hombre
            anillos -= enano

    return combinacion


def main():

    rings = input("¿Cuántos anillos quieres repartir en la Tierra Media?")
    combinacion = distributionOfRings(int(rings))
    if not combinacion:
        print(f"No hay posible combinación de {rings} anillos")
    else:
        for combineta in combinacion:
            print(combineta)


if __name__ == "__main__":
    main()
