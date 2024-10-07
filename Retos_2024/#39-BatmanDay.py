""" /*
* EJERCICIO:
 * Cada año se celebra el Batman Day durante la tercera semana de septiembre...
 * ¡Y este año cumple 85 años! Te propongo un reto doble:
 *
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta
 * su 100 aniversario.
 *
 * RETO 2:
 * Crea un programa que implemente el sistema de seguridad de la Batcueva.
 * Este sistema está diseñado para monitorear múltiples sensores distribuidos
 * por Gotham, detectar intrusos y activar respuestas automatizadas.
 * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa
 * que procese estos datos para tomar decisiones estratégicas.
 * Requisitos:
 * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 * - Cada sensor se identifica con una coordenada(x, y) y un nivel
 *   de amenaza entre 0 a 10 (número entero).
 * - Batman debe concentrar recursos en el área más crítica de Gotham.
 * - El programa recibe un listado de tuplas representando coordenadas de los
 *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
 *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 * Acciones:
 * - Identifica el área con mayor concentración de amenazas
 *   (sumatorio de amenazas en una cuadrícula 3x3).
 * - Si el sumatorio de amenazas es mayor al umbral, activa el
 *   protocolo de seguridad.
 * - Calcula la distancia desde la Batcueva, situada en(0, 0). La distancia es
 *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
 *   sus amenazas, la distancia a la Batcueva y si se debe activar el
 *   protocolo de seguridad.
 */ """

import datetime
import numpy as np
import random as rnd
from random import randint
import math


# Reto 1


def aniversary(year: int, day_of_times: int):

    any_date_in_month = datetime.datetime(year, 9, 6)

    year_month = any_date_in_month.strftime('%Y-%m')
    third_saturday = np.busday_offset(
        year_month, 2, roll='forward', weekmask='Sat')

    print(f"{day_of_times}:{third_saturday}")
    day_of_times += 1
    year += 1
    if day_of_times <= 100:
        aniversary(year, day_of_times)

# Reto 2


def security_system():
    matrix = [[rnd.randint(0, 10)for i in range(20)] for j in range(20)]
    print(np.matrix(matrix))

    max_threat_sum = 0
    centerX = 0
    centerY = 0

    for i in range(0, 17):
        for j in range(0, 17):
            threat_sum = calculate_threat(matrix, i, j)
            if (threat_sum > max_threat_sum):
                max_threat_sum = threat_sum
                centerX = i + 1
                centerY = j + 1

    # Caluclar Distancia absoluta
    # distance_batcave = math.abs(centerX) + math.abs(centerY)

    print(f"Grid con mas amenaza {centerX},{centerY}")
    print(f"Suma de amenazas: {max_threat_sum}")
    # print(f"Distancia a la BatCueva: {distance_batcave}")


def calculate_threat(map: list, x: int, y: int):
    sum = 0
    for x in range(x + 3):
        for y in range(y + 3):
            sum += map[x][y]

    return sum


def main():
    print("Reto 1: Fechas del BatmanDay hasta el 100 aniversario")
    aniversary(2024, 85)
    print("Reto 2 BatSensores")
    security_system()


if __name__ == "__main__":
    main()
