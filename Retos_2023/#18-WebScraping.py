"""
/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 """

import requests
from bs4 import BeautifulSoup
 
# Making a GET request
r = requests.get('https://holamundo.day/')
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# Finding by id
s = soup.find('section', id='section-37c93060-be70-11ed-a6a0-03f7635e8df3')
articulo = s.find('article', class_='notion-page-content-inner')


for x in articulo:
    if x.text == ">_ Agenda 8 de mayo | “Hola Mundo” day":
        print(x.text)
        horario = x.find_next_siblings('blockquote')
        for lines in horario: 
            print(lines.text)
        
