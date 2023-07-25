"""
/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */
"""

T9Diccionary=[";.?!1","ABC2","DEF3","GHI4","JKL5","MNO6","PQRS7","TUV8","WXYZ9","0"]

def T9 (code:str)->str:
    T9Result=""
    T9word = code.split("-")
    for x in T9word:
        for i in T9Diccionary:
            if(i.find(x[0])!= -1):
               T9Result = T9Result + i[len(x)-1] if i[len(x)-1] != "0" else  T9Result + " "
    
    return T9Result
        
def main():

   print(T9("6-666-88-777-33-3-33-888-11")) #MOUREDEV.
   print(T9("44-666-555-2-0-6-88-66-3-666-1111")) #HOLA MUNDO!
   print(T9("7777-999-555-888-2-66-2-7777-0-777-88-555-33-7777-111")) #SYLVANAS RULES?
   print(T9("555-666-55-8-2-777-0-666-4-2-777")) #LOKTAR OGAR
   
if __name__ == "__main__":
    main()  