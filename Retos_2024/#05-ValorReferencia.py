""" /*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */ """

value1 = 10
value2 = 20

reference1 = [10, 20]
reference2 = [30, 40]

# El paso por valor, el valor de las variables no se modifican al cambiarlas dentro de la función.


def values(valor1, valor2):
    valor1, valor2 = valor2, valor1
    new_value1, new_value2 = valor1, valor2

    print(
        f"Paso por valor. Nuevos valores: 1:{new_value1},2:{new_value2}")


print(f"Paso por valor. Valores originales: 1:{value1},2:{value2} - ")


# El paso por referencia, el valor de las variables no se modifican al cambiarlas dentro de la función

def reference(referencia1, referencia2):
    referencia1, referencia2 = referencia2, referencia1
    new_reference1, new_reference2 = referencia1, referencia2

    print(
        f"Paso por referencia. Nuevos valores: 1:{new_reference1},2:{new_reference2}")


print(
    f"Paso por referencia. Valores originales: 1:{reference1},2:{reference2} -")
""" x = [10, 20, 30]


def funcion(entrada):
    entrada = []


funcion(x)
print(x) """


values(value1, value2)
reference(reference1, reference2)
