"""/*
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
 */
"""
import sys
import random as rand
from os import system


participantes = []
choice = ""


def partOperations(name:str,option:int)-> bool:
    result=""
    try:
        result = participantes.index(name)
    except ValueError:
        result = ""
    
    #add
    if option == 1 and result == "":
        participantes.append(name)
        return "OK"
    elif option == 1 and result != "":
        return "NOK"
        
    #remove
    if option == 2 and result == "":
        return "NOK"
    elif option == 2 and result != "":
        participantes.remove(name)
        return "OK"

    #show
    if name == "show" and option == 3:
        print(participantes)
        
    #go
    if name == "go" and option == 4:
        choice = rand.choice(participantes)
        participantes.remove(choice)
        print(f"El ganador del sorteo es:{choice}")
        
def display_menu(menu):
   
    for k, function in menu.items():
        print(k, function.__name__)

def add():
    print("Has seleccionado añadir participante") 

    part = input("Inserta el participante: ")
    comprobation = partOperations(part,1)
    if comprobation == "OK":
        print("Participante añadido correctamente")
    else:
        print("El participante ya existe")
    
    #system('cls')  # clears stdout


def delete():
    print("Has seleccionado borrar participante") 
    part = input("Inserta el participante a eliminar:")
    comprobation = partOperations(part,2)
    if comprobation == "OK":
        print("Participante eliminado correctamente")
    else:
        print("El participante no existe")
    
    #system('cls')  # clears stdout

def show():
    print("Has seleccionado mostrar participantes") 
    partOperations("show",3)
    #system('cls')  # clears stdout

def go():
    print("Has seleccionado iniciar el sorteo") 
    partOperations("go",4)
    #system('cls')  # clears stdout

def done():
    system('cls') 
    print("Goodbye")
    sys.exit()

def main():
    functions_names = [add, delete, show,go, done]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(
            input("Introduce el numero de la selección: "))  
        selected_value = menu_items[selection] 
        selected_value() 

if __name__ == "__main__":
    main()