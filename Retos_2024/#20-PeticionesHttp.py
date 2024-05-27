""" 
/*
* EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA(opcional):
 * Utilizando la PokéAPI(https: // pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */ 
"""
import requests
from bs4 import BeautifulSoup
from enum import Enum

# EJERCICIO

""" url = "http://maireles.net"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.title.string
print(title)


response_json = response.json
print(response_json) """

# EXTRA
# 35,cleafairy


class Poke_Statics(Enum):
    name = 1
    id = 2
    weight = 3
    height = 4
    types = 5
    game_indices = 6


def pokedex(poke: str):
    poke_results = {}
    poke_games = []
    url = "https://pokeapi.co/api/v2/pokemon/"
    url_extra = url + poke
    response_extra = requests.get(url_extra).json()
    poke_types = ""
    for data in Poke_Statics:

        if data.name == "types":
            for x in range(len(response_extra[data.name])):
                poke_types = poke_types + \
                    response_extra[data.name][x]["type"]["name"] + ","

            poke_results[data.name] = poke_types

        elif data.name == "game_indices":
            for x in range(len(response_extra[data.name])):
                poke_games.append(
                    response_extra[data.name][x]["version"]["name"])

        else:

            poke_results[data.name] = response_extra[data.name]

    print(poke_results)
    print(poke_games)


def poke_evolution(poke: str):
    poke_evolution_results = []
    url_species = "https://pokeapi.co/api/v2/pokemon-species/"
    url_species_extra = url_species + poke
    response_species_extra = requests.get(url_species_extra).json()
    poke_species = response_species_extra["evolution_chain"]["url"]

    response_evolution_extra = requests.get(poke_species).json()

    for x in range(len(response_evolution_extra["chain"]["evolves_to"])):
        poke_evolution = response_evolution_extra["chain"]["evolves_to"][x]["species"]["name"]
        poke_evolution_results.append(poke_evolution)

    print(poke_evolution_results)


def main():

    print("Consulta la pokedex")
    pokemon = input("Introduce el nombre o el id del pokemon:")
    pokedex(pokemon)
    poke_evolution(pokemon)


if __name__ == "__main__":

    main()
