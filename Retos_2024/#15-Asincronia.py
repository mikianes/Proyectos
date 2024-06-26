""" /*
* EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA(opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */
"""

import asyncio
import time


""" import threading
import time
from time import sleep


def counter(interval: int, timer: int, name: str):
    print(
        f"La ejecucion de {name} durara {timer} segundos, con un intervalo de {interval} segundos.")
    print(f"Inicio ejecucion {name}")
    for i in range(1, timer + 1):
        print(f"{name} ejecucion:{i}")
        time.sleep(interval)

    if i == timer:
        print(f"Ejecucion de {name} finalizada")


hiloD = threading.Thread(target=counter, args=(1, 1, "Funcion D",))
hiloC = threading.Thread(target=counter, args=(1, 3, "Funcion C",))
hiloB = threading.Thread(target=counter, args=(1, 2, "Funcion B",))
hiloA = threading.Thread(target=counter, args=(1, 1, "Funcion A",))


import asyncio
def main():

    hiloC.start()
    hiloB.start()
    hiloA.start()

    print(f'Thread still alive? {hiloC.is_alive()}')


if __name__ == "__main__":

    main() """


async def my_async_function(name: str, seconds: int):
    if isinstance(name, str) == False:
        raise TypeError('name must be a string')
    if isinstance(seconds, int) == False:
        raise TypeError('seconds must be an integer')

    print(f'{name} started at {time.strftime("%X")}, duration: {seconds} seconds.')
    await asyncio.sleep(seconds)
    print(f'{name} finished at {time.strftime("%X")}')

if __name__ == '__main__':
    asyncio.run(my_async_function(name='Taask 1', seconds=5))


# DIFICULTAD EXTRA (opcional):
# Utilizando el concepto de asincronía y la función anterior, crea
# el siguiente programa que ejecuta en este orden:
# - Una función C que dura 3 segundos.
# - Una función B que dura 2 segundos.
# - Una función A que dura 1 segundo.
# - Una función D que dura 1 segundo.
# - Las funciones C, B y A se ejecutan en paralelo.
# - La función D comienza su ejecución cuando las 3 anteriores han
#   finalizado.

if __name__ == '__main__':
    async def main():
        await asyncio.gather(
            my_async_function(name='Task C', seconds=3),
            my_async_function(name='Task B', seconds=2),
            my_async_function(name='Task A', seconds=1)
        )
        await my_async_function(name='Task D', seconds=1)

    asyncio.run(main())
