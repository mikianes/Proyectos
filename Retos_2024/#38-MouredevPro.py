""" /*
* EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https: // mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro(sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila(con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 */
 """

import csv
import os
import random
from random import randint
from prettytable import PrettyTable

participants = []
winners = []
bookWinner = []


def lottery(people: list):

    elected = 0

    # Ganador de subscripción
    award = ["Subscription"]
    elected = random.choice(people)
    people.remove(elected)
    winners.append(elected + award)

    # Ganador de un descuento
    award = ["Discount"]
    elected = random.choice(people)
    people.remove(elected)
    winners.append(elected + award)

    # Ganador de un libro ( solo si tiene status activo y no le ha tocado otro sorteo)
    award = ["Book"]
    elected = random.choice(people)
    people.remove(elected)
    winners.append(elected + award)


def on_screen(people: list, text: str):

    t = PrettyTable()
    t.field_names = people[0]
    for i in people[1:]:
        t.add_row(i)

    print(text)
    print(t)


def load_csv(archive: str) -> list:

    mydir = 'G:\Proyectos\Proyectos\Retos_2024'
    myfile = archive
    file_to_open = os.path.join(mydir, myfile)

    try:
        with open(file_to_open, newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                id_, email, status = row
                if status.strip().lower() == 'activo':
                    participants.append(
                        [id_.strip(), email.strip()])
        return participants
    except:
        print("No se puede abrir el archivo o no existe")


def main():

    participants = load_csv('mouredevpro.csv')
    participants.insert(0, {"id", "email"})
    on_screen(participants, "Participantes")
    lottery(participants[1:])
    winners.insert(0, ["id", "email", "award"])
    on_screen(winners, "Ganadores")


if __name__ == "__main__":
    main()
