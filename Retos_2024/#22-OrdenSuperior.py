""" 
/*
* EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje
 * creando ejemplos simples(a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA(opcional):
 * Dada una lista de estudiantes(con sus nombres, fecha de nacimiento y
                                 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */
"""
import datetime


alumn_list = [["Moure", "10/05/1985", [5, 6, 7, 8, 9]],
              ["Luis", "01/01/2000", [3.5, 6, 10, 9, 5]],
              ["Maria", "03/05/1999", [9.95, 7.75, 5, 6, 5]],
              ["Eva", "20/10/1995", [9.75, 10, 9.6, 9, 9]]]


def alumns(alum: dict, average, best_students, birth, best_quali):
    print("****Media por alumno****")
    average(alum, 0)
    print("\n****Alumnos con 9 o mas de media****")
    best_students(alum, average)
    print("\n****Alumnos ordenados por nacimiento (ascendente)")
    birth(alum)
    print("\n****Alumno con mejor nota**** ")
    best_quali(alum)


def average(alum: dict, option):
    alum_average = []

    for a in alum:
        alum_calculate = []
        alum_calculate.append(a[0])
        alum_calculate.append(sum(a[2])/(len(a[2])))
        alum_average.append(alum_calculate)

    if option == 0:
        for x in alum_average:
            print(f"Nombre: {x[0]}, Media: {x[1]}")
    elif option == 1:
        return alum_average


def best_students(alum: dict, average):
    best = average(alum, 1)
    best_average = []
    for x in best:
        if x[1] >= 9:
            best_average.append(x)

    for y in best_average:
        print(f"Nombre: {y[0]}, Media: {y[1]}")


def birth(alumn: dict):

    sorted_list = sorted(
        alumn, key=lambda t: datetime.datetime.strptime(t[1], '%d/%m/%Y'))

    for x in sorted_list:
        print(f"Nombre: {x[0]}, F.Nac:  {x[1]}, Notas: {x[2]}")


def best_quali(alumn: dict):

    hight_note = 0
    hight_note_alumn = []
    for x in alumn:
        hight = max(x[2])
        if hight > hight_note:
            hight_note = hight
            if len(hight_note_alumn) > 0:
                hight_note_alumn.pop()
            hight_note_alumn.append(x)
        elif hight == hight_note:
            hight_note = hight
            hight_note_alumn.append(x)

    for x in hight_note_alumn:
        print(f"Nombre: {x[0]}, F.Nac:  {x[1]}, Notas: {x[2]}")


alumns(alumn_list, average, best_students, birth, best_quali)
