"""
/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */
"""
import itertools
import math

lista = []
triple = []
pitagorico = []



def ternas ():
    ternas = []
    for a in range(1, 17):
        for b in range(1, 17):
            for c in range(1, 17):
                if a**2 + b**2 == c**2:
                    ternas.append((a, b, c))

    print('Cantidad de ternas:', len(ternas))

    for t in ternas:
        print(t)
    

def cuadrados (tar:int):

    #Crear la lista de números elevados   
    for num in range(1,tar +1,1):
        lista.append(int(math.pow(num,2)))
        
    lista.reverse()
    print("Numeros Elevados",lista)
    
    #Se buscan la suma de dos números sea igual a otro número de la lista
    for i in range(len(lista),0,-1):
        sum_multiple(lista,lista[i-1])
    
    print("Triple pitagórico",triple)
    
    #Se vuelve a obtener los números originales para mostrar el resultado.
    for x in range(len(triple)):
        suma = sum(triple[x])
        for i in (triple[x]):
            n = int(math.sqrt(i))
            pitagorico.append(n)
           
        pitagorico.append(int(math.sqrt(suma)))
    
    #Se divide el array cada 3 componentes  
    for i in range(0,len(pitagorico),3):
        x = i
        print(pitagorico[x:x + 3])
          

#Dado un rasultado, busca entre los componentes una suma. Se limita a la suma de 2 números.
def sum_multiple(numbers:list, target:int):

  result = [seq for i in range(len(numbers), 0, -1)
            for seq in itertools.combinations(numbers, i)
            if sum(seq) == target]

  resultado = list(set(result))
  
  for i in range(len(resultado)):
        if len(resultado[i]) == 2:
            triple.append(resultado[i])
                        
def main():
   
    cuadrados(20)
    print("---------")
    ternas()
    

if __name__ == "__main__":
    main() 