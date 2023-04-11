"""/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
 """

numero = 0
hexadict = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

def conversor (number,base):
    octal = []
    numero = number
    num = number
    while numero > 0:
        numero = int(num / base)
        resto = int(num % base)
        num = numero
        if base == 16:
            octal.append(hexadict[resto])
        else:
            octal.append(resto)
       
    octal.reverse()
    resultado = "".join(str(v) for v in octal)
    if base == 8:
        print(f"El octal de {number} es {resultado}")
    else:
        print(f"El hexadecimal de {number} es {resultado}")
        
def main():
   
    print("Octales")
    conversor(1000,8)
    conversor(95,8)
    conversor(10,8)
    conversor(300,8)
    conversor(94260,8)
    conversor(100,8)
    print("Hexadecimales")
    conversor(1000,16)
    conversor(95,16)
    conversor(10,16)
    conversor(300,16)
    conversor(94260,16)
    conversor(100,16)
    
if __name__ == "__main__":
    main() 