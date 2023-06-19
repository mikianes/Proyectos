"""
/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
 
 En criptografía, el cifrado César, también conocido como cifrado por desplazamiento, código de César o desplazamiento de César, 
 es una de las técnicas de cifrado más simples y más usadas. Es un tipo de cifrado por sustitución en el que una letra en el texto original 
 es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto. 
 Por ejemplo, con un desplazamiento de 3, la A sería sustituida por la D (situada 3 lugares a la derecha de la A), la B sería reemplazada por la E, etc. 
 
"""

caesar = ["a","b","c","d","e","f","g","h","i","j", 
            "k","l","m","n","ñ","o","p","q","r","s", 
            "t","u","v","w","x","y","z"]
                   
def conmutatio(text,clave,forma):
    
    eventum = ""
    
    #Recorrer el texto y buscar su  correspondiente en el diccionario
    for character in text:
        if character == ",":
            eventum = eventum + ","
        elif character == " ":
            eventum = eventum + " "
        elif forma == "e":
            index = caesar.index(character)
            if index + int(clave) > len(caesar):
                position = (index + int(clave) - len(caesar))
                #print(character + ":" + str(caesar.index(character)) + " -> " + caesar[position] + ":" + str(caesar.index(caesar[position])+1))
                eventum = eventum + caesar[position]
            else:
                #print(character + ":" + str(caesar.index(character)) + " -> " + caesar[index + int(clave)] + ":" + str(caesar.index(caesar[index + int(clave)])))
                eventum = eventum + caesar[index + int(clave)]
        else:
            indexDesencriptar = caesar.index(character)
            if indexDesencriptar - int(clave) < 0:
                positionDesencriptar = len(caesar) - (indexDesencriptar  - int(clave))*-1
                eventum = eventum + caesar[positionDesencriptar]
            else:
                eventum = eventum + caesar[indexDesencriptar - int(clave)]

    print(eventum)            
        
def main():
    
    forma = input("Escribe d para desencriptar o e para encriptar:")
    clavis = input("Introduce el número clave:")
    verbum = input("Palabra o texto a cifrar:")
    conmutatio(verbum.lower(),int(clavis),forma.lower())
   
if __name__ == "__main__":
    main()  