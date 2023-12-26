"""
/*
 * Todo llega a su fin... Este es el último reto de programación 
 * semanal de 2023.
 *
 * Crea un programa que muestre un listado calculado en tiempo real
 * con todos los usuarios que han resuelto algún reto de programación
 * de este año.
 * - El listado debe estar ordenado por el número de ejercicios resueltos
 *   por cada usuario (y mostrar ese contador al lado de su nombre).
 * - También se debe de mostrar el número de usuarios que han participado
 *   y el número de correcciones enviadas.
 *
 * Muchísimas gracias por ayudar a crear este gran recurso
 * para la comunidad... ¡Prepárate para 2024!   
 */
"""
import json
import requests
from requests.auth import HTTPBasicAuth
all_contributors = list()
page_count = 1
personas = {}
count_contributions = 0
while True:
    contributors = requests.get(
        "https://api.github.com/repos/mouredev/retos-programacion-2023/contributors?page=%d" % page_count, auth=HTTPBasicAuth('mikianes', 'Mike1983Bar3'))
    if contributors != None and contributors.status_code == 200 and len(contributors.json()) > 0:
        all_contributors = all_contributors + contributors.json()
        response_data = contributors.json()
        for item in response_data:
            # personas.append(item['login'])
            personas.update({item['login']: item['contributions']})
            count_contributions = count_contributions + item['contributions']

    else:
        break
    page_count = page_count + 1
count = len(all_contributors)
print(personas)
# print(count_contributions)
# print("-------------------%d" % count)
print("--------------------------------")
print(
    f"Han participado {count} personas enviado {count_contributions} correcciones en total.")
