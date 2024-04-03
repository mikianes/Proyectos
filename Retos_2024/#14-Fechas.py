""" /*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */ """

from dateutil.relativedelta import relativedelta
from datetime import datetime, date


days = ["Lunes", "Martes", "Miercoles",
        "Jueves", "Viernes", "Sabado", "Domingo"]
"""
    Ejercicio
"""

# fecha actual
ahora = datetime.now()

fecha_str = "1983-03-10 17:30:00"
datetime_format = "%Y-%m-%d %H:%M:%S"

fecha = datetime.strptime(fecha_str, datetime_format)

# utilizamos el modulo para restar correctamente
edad = relativedelta(ahora, fecha)
print("EJERCICIO")
print(
    f" 1. Tienes {edad.years} años, {edad.months} meses, {edad.days} días, {edad.hours} horas, {edad.minutes}, {edad.seconds} segundos")
print("EXTRA")
print("1. Día de la semana")
print(days[fecha.weekday()])
print(fecha.strftime("%A"))
print("2. Día del año")
print(fecha.strftime("%j"))
print("3. Nombre del mes")
print(fecha.strftime("%B"))
print(fecha.strftime("%b"))
print("4.Número de la semana")
print(fecha.strftime("%W"))
print("5. Versión local de fecha")
print(fecha.strftime("%x"))
print("6. Version local Fecha y Hora")
print(fecha.strftime("%c"))
print("7. Siglo")
print(fecha.strftime("%C"))
print("8 HH:MM:SS")
print(fecha.strftime("%H:%M:%S"))
print("9. Timezone")
print(fecha.strftime("%Z"))
