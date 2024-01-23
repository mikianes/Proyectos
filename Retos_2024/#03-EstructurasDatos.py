"""  
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa. 
"""
# Listas
# Creación
colores = ['Rojo', 'Verde', 'Azul', 'Amarillo']
# Inserción
colores.append('Blanco')
# Elimina el último y lo muestra
colores.pop()
# Elimina el elemento de la posición
colores.pop(len(colores)-1)
# Ordena los elementos
colores.sort()
print(colores)
print('--------------------------------')
print('DIFICULTAD EXTRA')

global_agenda = []


def number_verification() -> int:
    while True:
        try:
            number = int(
                input("Telefono (Maximo 11 caracteres):"))
        except ValueError:
            print("Debes introducir un numero")
            continue

        if not number:
            print("Debes introducir un numero")
            continue
        if len(str(number)) > 11:
            print("El numero no puede ser mayor de 11 caracteres")
            continue
        else:
            break

    return number


def multiSearch(name: str, option: int):
    print("MultiSearch")
    search = name
    for sublist in global_agenda:
        if sublist[0] == search:
            match option:
                case 1:
                    print(sublist)
                    break
                case 3:
                    new_name = input("Introduce el nuevo nombre:")
                    new_phone = input("Introduce el nuevo telefono:")
                    sublist[0] = new_name
                    sublist[1] = new_phone
                    print(global_agenda)
                    break
                case 4:
                    global_agenda.pop(global_agenda.index(sublist))
                    print(global_agenda)
                    break

    extra()


def insert():
    name = input("Nombre:")
    phone = number_verification()

    newRecord = []
    newRecord.append(name)
    newRecord.append(phone)
    global_agenda.append(newRecord)
    print(global_agenda)
    extra()


def option(opt: int):

    match opt:
        case 1:
            print('----Buscar----')
            name = input("Introduce el contacto a buscar:")
            multiSearch(name, 1)
        case 2:
            print('----Insertar----')
            insert()
        case 3:
            print('----Actualizar----')
            name = input("Introduce el contacto a modificar:")
            multiSearch(name, 3)
        case 4:
            print('----Eliminar----')
            name = input("Introduce el contacto a eliminar:")
            multiSearch(name, 4)
        case 5:
            print('----Listado-----')
            print(global_agenda)
            extra()
        case 6:
            print('----Salir----')
            exit()


def extra():

    print('Agenda de contactos')
    print('1. Busqueda')
    print('2. Insertar')
    print('3. Actualizar')
    print('4. Eliminar')
    print('5. Listado')
    print('6. Salir')
    election = int(input("Introduce la opcion deseada:"))
    option(election)


def main():

    count = extra()


if __name__ == "__main__":

    main()
