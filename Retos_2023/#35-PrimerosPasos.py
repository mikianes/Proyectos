"""/*
 * Como cada año, el día 256 se celebra el "Día de la Programación".
 * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos 
 * 256 regalos para seguir aprendiendo programación:
 * https://diadelaprogramacion.com
 *
 * Para seguir ayudando, te propongo este reto:
 * Mostrar la sintaxis de los principales elementos de un lenguaje
 * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
 *
 * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
 * y comenta cada bloque para identificar con qué se corresponde:
 * - Haz un "Hola, mundo!"
 * - Crea variables de tipo String, numéricas (enteras y decimales)
 *   y Booleanas (o cualquier tipo de dato primitivo).
 * - Crea una constante.
 * - Usa un if, else if y else.
 * - Crea estructuras como un array, lista, tupla, set y diccionario.
 * - Usa un for, foreach y un while.
 * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
 * - Crea una clase.
 * - Muestra el control de excepciones.
 *
 * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
 * de sintaxis básica de muchos lenguajes.
 *
 * ¡Muchas gracias!
 */"""
 
 # Punto 1: Hola, mundo!
print("Hola, mundo!")

# Punto 2: Crea una variable de texto o string
mi_texto = "¡Hola desde Python!"

# Punto 3: Crea una variable de número entero
mi_entero = 42

# Punto 4: Crea una variable de número con decimales
mi_decimal = 3.14

# Punto 5: Crea una variable de tipo booleano
mi_booleano = True

# Punto 6: Crea una constante (las constantes en Python son convenciones)
MI_CONSTANTE = 10

# Punto 7: Usa un if, else if y else
if mi_entero > 50:
    print("El número es mayor que 50")
elif mi_entero < 50:
    print("El número es menor que 50")
else:
    print("El número es igual a 50")

# Punto 8: Crea un Array (lista en Python)
mi_lista = [1, 2, 3, 4, 5]

# Punto 9: Crea una lista
mi_lista_texto = ["Manzana", "Banana", "Naranja"]

# Punto 10: Crea una tupla
mi_tupla = (1, "Tupla")

# Punto 11: Crea un set
mi_set = {"Rojo", "Verde", "Azul"}

# Punto 12: Crea un diccionario
mi_diccionario = {
    "clave1": "valor1",
    "clave2": "valor2"
}

# Punto 13: Usa un ciclo for
for elemento in mi_lista:
    print(elemento)

# Punto 14: Usa un ciclo foreach
for elemento in mi_lista_texto:
    print(elemento)

# Punto 15: Usa un ciclo while
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# Punto 16: Crea una función sin parámetros que no retorne nada
def funcion_sin_parametros():
    print("Función sin parámetros")

# Punto 17: Crea una función con parámetros que no retorne nada
def funcion_con_parametros(param1, param2):
    print("Parámetro 1:", param1)
    print("Parámetro 2:", param2)

# Punto 18: Crea una función con parámetros que retorne valor
def funcion_con_retorno(a, b):
    return a + b

# Punto 19: Crea una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Punto 20: Muestra control de excepciones
try:
    resultado = mi_entero / 0
except Exception as e:
    print("Error:", e)