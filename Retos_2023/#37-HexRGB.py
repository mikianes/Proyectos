"""
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
"""
import re
import math

numero = 0
hexadict = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
decimaldict = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

def conversorRGB(cadena:str):
   
    rgb = []
    calc = []
    rgbString = cadena.replace("#","")
    
    if len(cadena)< 7 or len(cadena) > 7:
        print("La cadena no es correcta")
    else:
        rgb = re.findall("..",rgbString)
       
        for x in rgb:
           character = x [::-1]
           
           num = 0
           for index in range(len(character)):
               char = character[index]
               potencia = math.ceil(pow(16,index))
               
               if char.isdigit():
                    num = num + decimaldict[int(char)] * potencia
               else:
                    num = num +  decimaldict [char.upper()] * potencia
                   
               if index == len(character)-1:
                    calc.append(num)
        
        print(f"HEX a RGB:","hex:",cadena,"->" ,"r:",calc[0],"g:",calc[1],"b:",calc[2])
                      
        
def conversorHexa (num1,num2,num3):
    
    hexa = []
    hex = []
    resultado = ""
    hex.append(num1)
    hex.append(num2)
    hex.append(num3)
    
    for x in hex:
        numero = x
        num = x
    
        if x == 0:
            hexa.append("00")
            
    
        while numero >0:
            numero = int(num / 16)
            resto = int(num % 16)
            num = numero
            hexa.append(hexadict[resto]) 
           
        hexa.reverse()
        resultado = resultado + "".join(map(str,hexa))
        hexa = []
        
       
    print(f"RGB a HEX:","r:", num1 , "g:", num2 , "b:",num3,"->", "#" + resultado)
     


def main():
   
    print("Ejemplo 1")
    conversorHexa(51,102,255)
    conversorRGB("#3366ff")
    
    print("Ejemplo2")
    conversorHexa(63,81,181)
    conversorRGB("#3F51B5")
    
    print("Ejemplo3")
    conversorHexa(255,152,0)
    conversorRGB("#FF9800")
    
    print("Ejemplo4")
    conversorHexa(255,251,238)
    conversorRGB("#FFFBEE")
    
    print("Ejemplo5")
    conversorHexa(62,39,35)
    conversorRGB("#3E2723")
    
    print("Ejemplo6")
    conversorHexa(0,0,0)
    conversorRGB("#000000")
    
    
    
if __name__ == "__main__":
    main() 