"""
/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */
"""
gemelos = []
cont = 0 #Solo es primo si el valor es 2, el mismo número y 1
numero = int(input("Ingrese un numero a evaluar: "))
for n in range(2, numero + 1):
    for d in range(1, n + 1):
        if n % d == 0:
            cont += 1
    if cont == 2:
        gemelos.append(n)
    cont = 0

 
for i in range(len(gemelos)):
    twin = gemelos[i]+2
    if i < len(gemelos)-1:
        if gemelos[i+1] == twin:
            print(f"({gemelos[i]},{gemelos[i+1]}),",end=" ")
           
           
print("Fin")