"""
/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */
"""
import locale

def read_abacus_number(abacus: list)-> str:
    if len(abacus) != 7:
        raise Exception("Tamaño total incorrecto")
    
    number = ""
    
    for row in abacus:
        if len(row) == 12 and "---" in row and row.replace("---", "") == "OOOOOOOOO":
            number += str(len(row.split("---")[0]))
        else:
            raise Exception("Formato de fila incorrecto")

    return "{:,}".format(int(number)).replace(",", ".")




abacus = ["O---OOOOOOOO",
          "OOO---OOOOOO",
          "---OOOOOOOOO",
          "OO---OOOOOOO",
          "OOOOOOO---OO",
          "OOOOOOOOO---",
          "---OOOOOOOOO"]

# abacus = ["OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---",
#           "OOOOOOOOO---"]

# abacus = ["---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO"]

# abacus = ["---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "O---OOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO",
#           "---OOOOOOOOO"]

print(read_abacus_number(abacus))