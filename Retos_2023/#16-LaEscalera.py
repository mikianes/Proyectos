"""
/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */
"""

def escalera(step):
    stepby = step
    spaces = (stepby *2) 
    if stepby > 0:   
        for i in range(step+1):
            if i == 0:
                escalon = " _"
                print(escalon.rjust(spaces+1))
            else:
                escalon = "_|"
                print(escalon.rjust(spaces))
                spaces -= 2
    elif stepby < 0:
        step = step * -1
        spaces = 2
        for i in range(step+1):
            if i == 0:
                escalon = " _"
                print(escalon.rjust(spaces))
                spaces += 2
            else:
                escalon = "|_"
                print(escalon.rjust(spaces))
                spaces += 2
    else:
        print("__")

def main():
    escalera(4)
    escalera(-4)
    escalera(0)
    escalera(10)
    
if __name__ == "__main__":
    main() 