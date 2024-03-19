""" /*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos. """

import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
from bs4 import BeautifulSoup
import os


def create():
    # JSON
    datos = {"nombre": "Pedro", "fecha de Nacimiento": "10/2/1983",
             "Lenguajes de programacion": ["Python", "Java", "SQL"]}
    datos_jason = json.dumps(datos)
    # print(datos_jason)

    with open("json_ex.json", "w") as file:
        json.dump(datos, file)

    # XML
    m_encoding = "UTF-8"
    lenguajes_programacion = ["Python", "Java", "SQL"]

    root = ET.Element("Agenda")
    persona = ET.SubElement(root, "Persona")
    ET.SubElement(persona, "Nombre", nombre="Pedro").text = "Pedro"
    ET.SubElement(persona, "Edad", edad="41").text = "41"

    for lenguaje in lenguajes_programacion:
        LengDev = ET.SubElement(persona, "Lenguajes")
        LengDev.text = lenguaje

    dom = xml.dom.minidom.parseString(ET.tostring(root))
    xml_string = dom.toprettyxml()
    part1, part2 = xml_string.split("?>")

    with open("xml_ex.xml", "w") as xfile:
        xfile.write(part1 + "encoding=\"{}\"?>\n".format(m_encoding) + part2)
        xfile.close()


def read():

    # JSON
    with open("json_ex.json") as file:
        data = json.load(file)

    print("Fichero JSON")
    print(data)

    # XML
    bs = BeautifulSoup(open("xml_ex.xml"), "xml")
    print("Fichero XML")
    print(bs.prettify())


def option(opt: int):

    match opt:
        case 1:
            create()
        case 2:
            read()
        case 3:
            os.remove("json_ex.json")
            os.remove("xml_ex.xml")
            exit()


def extra():

    print("1. Crear Ficheros JSON y XML")
    print("2. Leer Ficheros JXON y XML")
    print("3. Salir y Borrar los archivos")
    election = int(input("Introduce la opcion deseada:"))

    option(election)


def main():

    extra()


if __name__ == "__main__":

    main()
