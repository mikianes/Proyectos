""" /*
* EJERCICIO:
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * Desarrolla un programa que se conecte al API de Spotify y los compare.
 * Requisitos:
 * 1. Crea una cuenta de desarrollo en https: // developer.spotify.com.
 * 2. Conéctate al API utilizando tu lenguaje de programación.
 * 3. Recupera datos de los endpoint que tú quieras.
 * Acciones:
 * 1. Accede a las estadísticas de las dos bandas.
 *    Por ejemplo: número total de seguidores, escuchas mensuales,
 *    canción con más reproducciones...
 * 2. Compara los resultados de, por lo menos, 3 endpoint.
 * 3. Muestra todos los resultados por consola para notificar al usuario.
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular.
 */
 """

# Linkin Park : 6XyY86QOPPrYVGvF9ch6wz
# Oasis : 2DaxqgrOhkeH0fpeiQq2f4

import requests
import json
from prettytable import PrettyTable

CLIENT_ID = 'MIRALO EN SPOTY'
CLIENT_SECRET = 'MIRALO EN SPOTY'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

total = []


def spotifyPodium(id: str, total: list):

    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    # Track ID from the URI
    track_id = id

    # Get Artistas
    r = requests.get(BASE_URL + 'artists/' + track_id, headers=headers)
    r = r.json()

    # Get número de canciones totales ( límite 25 albumes )
    x = requests.get(BASE_URL + 'artists/' + track_id +
                     '/albums?limit=25', headers=headers)
    x = x.json()
    result = [i['total_tracks'] for i in x['items']]

    artist = []
    artist.append(r['name'])
    artist.append(r['popularity'])
    artist.append(r['followers']['total'])
    artist.append(sum(result))
    total.append(artist)


def onScreen(total: list):

    t = PrettyTable()
    t.field_names = ["Grupo", "Popularidad", "Seguidores", "Canciones"]
    for i in total:
        t.add_row(i)

    print(t)

    print(
        f"El grupo mas popular es: {max(total, key=lambda x: x[1])[0]} con una popularidad de {max(total, key=lambda x: x[1])[1]}.")

    print(
        f"El grupo con mas seguidores es: {max(total, key=lambda x: x[2])[0]} con {max(total, key=lambda x: x[2])[2]} seguidores.")

    print(
        f"El grupo con mas canciones es: {max(total, key=lambda x: x[3])[0]} con {max(total, key=lambda x: x[3])[3]} canciones.")


def main():

    spotifyPodium("6XyY86QOPPrYVGvF9ch6wz", total)
    spotifyPodium("2DaxqgrOhkeH0fpeiQq2f4", total)
    spotifyPodium("0U5P1naxYkkOsbHIGkVU9c", total)
    spotifyPodium("6qqNVTkY8uBg9cP3Jd7DAH", total)
    onScreen(total)


if __name__ == "__main__":
    main()
