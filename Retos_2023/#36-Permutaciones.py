"""
/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */
 Algoritmo HEAP (https://es.wikipedia.org/wiki/Algoritmo_de_Heap)
 
"""

import itertools

#Incompleta    
def generacion(n:int, lista:list):
    res = lista
    if n == 1:
        return lista
    else:
        for x in range(0,n):
            generacion(n - 1, res)
            if n % 2 == 0:
                res[x], res[n-1] = res[n-1], res[x]
            else:
                res[1], res[n-1] = res[n-1], res[1]
    print(res)
                

#Version desde TypeScript
def permaType(cadena:str, prefix:str=""):
    CONSTLEN = len(cadena)
    if(CONSTLEN == 0):
        print(prefix)
    else:
        for x in range(0,CONSTLEN):
            CONSTREST = cadena[slice(0:x)] + cadena[slice(x+1)]
            permaType(CONSTREST,prefix + cadena[x])
            
    return prefix
        
#Con las herramientas del lenguaje
def permutations():
   word = list(itertools.permutations("sol"))
   print(word)
   
""" 
# Python function to print permutations of a given list
def permutation(lst):

	# Si la lista está vacía no hay permutaciones
	if len(lst) == 0:
		return []

	# Si la lista tiene un elemento, solo es posible una permutación
	if len(lst) == 1:
		return [lst]

	# Find the permutations for lst if there are
	# more than 1 characters

	l = [] # Lista vacía que almacenará la permutación actual

	# Itera la lista de entrada y calcula la permutación
	for i in range(len(lst)):
	    m = lst[i]

	# Extract lst[i] or m from the list. remLst is
	# remaining list
	    remLst = lst[:i] + lst[i+1:]

	# Generating all permutations where m is first
	# element
	    for p in permutation(remLst):
		    l.append([m] + p)
    
      
	return l
"""

# Driver program to test above function
#data = list('sol')
#for p in permutation(data):
	#print (p)


#generacion(3,lista=list("sol")) 
#permutations()

#Versión TypeScript
permaType("sol")
