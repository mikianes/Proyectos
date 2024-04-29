""" /*
* EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA(opcional):
 * Crea 3 expresiones regulares(a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
"""

import re

# Ejercicio
texto = "Hola, tengo 41 años y he estado a -10 grados una vez en la sierra."
x = re.findall(
    r'[+-]?\d+', texto)

print(f"Ejercicio: {texto}, resultado: {x}")

# Dificultad Extra
mail = "moure.dev@mouredev.com.es"
phone = "123456789"
url = "https://mouredev.com/"

extra_one = re.findall(r'^\w[a-zA-Z]\S+@\S+\.\S+\w[a-zA-Z]+$', mail)
try:
    if len(mail) == len(extra_one[0]):
        result_one = "OK"
    else:
        result_one = "NOK"
except:
    result_one = "NOK"
print(f"Ejercicio Extra 1: {mail}, resultado: {extra_one}", result_one)

extra_two = re.findall(r'^\+?[\d\s]{3,}', phone)
try:
    if len(phone) == len(extra_two[0]):
        result_two = "OK"
    else:
        result_two = "NOK"
except:
    result_two = "NOK"
print(f"Ejercicio Extra 2: {phone}, resultado: {extra_two}", result_two)
