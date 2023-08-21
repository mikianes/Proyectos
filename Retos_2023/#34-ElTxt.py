"""
/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.  
 */
"""
import glob
from pathlib import Path

def file_comprobation ():
    
    files = glob.glob('text.txt')
    if len(files) == 0:
        files = open('text.txt','x')
        print("Fichero creado")
        file_writing(False)
    else:
        print("El Fichero ya está creado.")
        opcion = input("¿Desea borrar el contenido (B) o continuar escribiendo (E)?:")
        if opcion.upper() == "B":
           file_remove("text.txt")
           file_writing(False)
        elif opcion.upper() == "E":
           file_reading()
           file_writing(True)
        else:
            print("Opción errónea")
            
def file_reading():
    f = open('text.txt','r')
    print(f.read())
    print("-------")
    
 
def file_writing(add:bool):
    f = open('text.txt','a')
    texto = input("Escribe:")
    if add == True:
        f.write("\n" + texto)
    else:
        f.write(texto)          
            
def file_remove(file):
    files = open(file,"w") 
    files.close()
               
def main(): 
    file_comprobation()
   
if __name__ == "__main__":
    main()