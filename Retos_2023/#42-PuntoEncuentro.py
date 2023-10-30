"""
/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */    
    
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def coord(coordA:list,velA:list,coordB:list,velB:list):
 
    if velA == velB:
        print("Los puntos nunca se encontrarán")
        exit()
    else:
        print("Entro2")
        


def prueba():
    
    x = np.linspace(0, 2, 100)
    #Generamos una grafica lineal para una recta en X
    plt.plot(x, x, label='linear')
    #Generamos otra grafica lineal para una X cuadratica
    plt.plot(x, x**2, label='quadratic')
    #Generamos una grafica lineas para una X Cubica
    plt.plot(x, x**3, label='cubic')
    #Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title("Simple Plot")
    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()


def main():
    coordA = []
    coordB = []
    velA = []
    velB = []
         
    xA = input("Introduce la coordenada X del primer objeto:")
    yA = input("Introduce la coordenada Y del primer objeto:")
    xvA = input("Introduce la velocidad de desplacamiento X del primer objeto:")
    yvA = input("Introduce la velocidad de desplacamiento Y del primer objeto:")
   
    xB = input("Introduce la coordenada X del segundo objeto:")
    yB = input("Introduce la coordenada Y del segundo objeto:")
    xvB = input("Introduce la velocidad de desplacamiento X del segundo objeto:")
    yvB = input("Introduce la velocidad de desplacamiento Y del segundo objeto:")
    
    #prueba()
    
    coordA.append(xA)
    coordA.append(yA)
    velA.append(xvA)
    velA.append(yvA)
    
    coordB.append(xB)
    coordB.append(yB)
    velB.append(xvB)
    velB.append(yvB)
   
    coord(coordA,velA,coordB,velB)
    
if __name__ == "__main__":
    main() 