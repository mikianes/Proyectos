"""
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
*/
"""
import calendar

def mes(mes):
    resultado = {"enero":"1","febrero":"2","marzo":"3",
                 "abril":"4","mayo":"5","junio":"6",
                 "julio":"7","agosto":"8","septiembre":"9",
                 "octubre":"10","noviembre":"11","diciembre":"12"}
    
    try:
        return resultado[mes.lower()]
    except KeyError as ke:
        print("El mes no existe", ke)
        exit()
    
def friday(m,a):
        
    if m.isnumeric():
       m = m
    else:
       resultado = mes(m.lower())
       print(resultado)
       m = resultado
        
    c = calendar.TextCalendar(calendar.MONDAY)
    str = c.formatmonth(int(a),int(m))
    print(str)
    
    dia = calendar.weekday(int(a),int(m),13)
    if dia != 4:
        print("No hay Viernes 13")
    else:
        print("Hay viernes 13")

def main():
    mes = input ("Introduce el mes:")
    month = mes.lower()
    anio = input ("Introduce el año:")
    year = anio.lower()
    friday(month,year)
    
if __name__ == "__main__":
    main()  