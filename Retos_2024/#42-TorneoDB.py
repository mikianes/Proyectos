""" /*
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa ---- OK
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud. ---- OK
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores. 
 * - El luchador con más velocidad comienza atacando. ---- OK
 * - El daño se calcula restando el daño de ataque del ---- OK
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque. ---- OK
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque. ---- OK
 * - Después de cada turno y ataque, el oponente pierde salud. ---- OK
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2. ---- OK
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
 */ """

import random
import numpy
from prettytable import PrettyTable

full_list_participants = []
# Lista para evitar tener que introducir los datos mientras se desarrolla. La longitud tiene que ser potencia de 2
# ["Nombre", "Velocidad", "Ataque", "Defensa", "Salud"]
full_list_participants_demo = [["Gohan", 40, 32, 35, 100], [
    "Cell", 30, 42, 45, 100], ["Goku", 20, 42, 30, 100], ["Piccolo", 21, 32, 40, 100]]


class PowerError(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self) -> str:
        return "Error, no es una potencia de 2: " + str(self.valor)


class Participants():
    def __init__(self, name: str, speed: int, attack: int, defense: int, health: int):
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health = health

    def add_new_participant(self):
        participant = [self.name, self.speed,
                       self.attack, self.defense, self.health]
        full_list_participants.append(participant)


def onScreen(total: list):

    t = PrettyTable()
    t.field_names = ["Nombre", "Velocidad", "Ataque", "Defensa", "Salud"]
    for i in total:
        t.add_row(i)

    print(t)


def lets_fight(list_fighters: list, start: bool):

    print("Luchadores")
    onScreen(list_fighters)

    # Ataca primero el que tiene mayor velocidad.
    if list_fighters[0][1] > list_fighters[1][1] and start == True:
        # Calculo de probabilidad del 20%
        start = False
        probability = numpy.random.choice(
            [list_fighters[0][0], list_fighters[1][0]], size=1, p=[0.8, 0.2])
        if probability == list_fighters[1][0]:
            list_fighters[1][4] = list_fighters[1][4]
            print("20%")
        # Calculo del 10% si la defensa es mayor
        elif list_fighters[1][3] > list_fighters[0][2]:
            defense = list_fighters[1][3]
            health = list_fighters[1][4]
            list_fighters[1][4] = int(health -
                                      defense*0.1)
        else:
            list_fighters[1][4] = list_fighters[1][4] - \
                (list_fighters[0][2] - list_fighters[1][3])
    else:
        start = False
        # Calculo de probabilidad del 20%
        probability = numpy.random.choice(
            [list_fighters[1][0], list_fighters[0][0]], size=1, p=[0.8, 0.2])
        if probability == list_fighters[0][0]:
            list_fighters[0][4] = list_fighters[0][4]
            print("20%")
        # Calculo del 10% si la defensa es mayor
        elif list_fighters[0][3] > list_fighters[1][2]:
            defense = list_fighters[0][3]
            health = list_fighters[0][4]
            list_fighters[0][4] = int(health -
                                      defense*0.1)
        else:
            list_fighters[0][4] = list_fighters[0][4] - \
                (list_fighters[1][2] - list_fighters[0][3])

    print("Resultados Finales")
    onScreen(list_fighters)


def get_combats(list_participants: list):
    combat = random.sample(list_participants, 2)
    lets_fight(combat, True)


def is_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1


def get_fighters(number: int):
    pass
    counter = 0
    while counter < number:
        try:
            name = input("Nombre:")
            speed = int(input("Velocidad:"))
            attack = int(input("Ataque:"))
            defense = int(input("Defensa:"))
            health = 100

            fighters = Participants(name, speed, attack, defense, health)
            fighters.add_new_participant()
            counter += 1

        except ValueError:
            print("Los datos no son correctos")


def define_participants():
    while True:
        try:
            participants = int(input(
                "Cuantos luchadores participaran en el torneo?"))
            if is_power_of_two(participants):
                # print(f"{participants} is a power of two.")
                get_fighters(participants)
                break
            else:
                raise PowerError(participants)
        except ValueError:
            print("No es un número")
        except PowerError as e:
            print(e)


def main():

    # define_participants()
    # print(full_list_participants)
    get_combats(full_list_participants_demo)


if __name__ == "__main__":
    main()
