"""
/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */    
"""
import numpy as np

up = "+2"
down = "-2"
equal = "0"
temperatures = []

def weather (days:int, temp_Ini:int, prop_Rain:int):
    temp_Max = 0
    temp_Min = 0
    rain_Days = 0
    prob = np.random.choice([up, down, equal], size = days, p=[0.1,0.1,0.8])
    temp = temp_Ini
    rain = prop_Rain
    rainDay = "No"
    print(prob)
    
    for num in range(1,days +1):
        
        temp = temp + int(prob[num-1])
        temperatures.append(temp)
        
        
        if temp > 25:
            rain = rain +20
        elif temp < 5:
            rain = rain -20
            
        if rain >= 100:
            temp = temp -1
            rain = 100
            rain_Days += 1
            rainDay="Si"
        elif rain <= 0:
            rain = 0
            rainDay="No"
            
        print(f"Día: {num} , temp: {temp}, Prob Rain: {rain}, ¿Llueve?: {rainDay} , Prob: {prob[num-1]}")
    
    print(f"Max Temp: {max(temperatures)},Min Temp: {min(temperatures)},Rain Days: {rain_Days}")
    
    
        

def main():
    #print(prob)
    day = input("¿Cuandos días quieres predecir? : ")
    temp_Ini = input("¿Cual es la temperatura? : ")
    prop_Rain = input("¿Cual es la probabilidad de lluvia? : ")
    weather(int(day),int(temp_Ini),int(prop_Rain))
    
if __name__ == "__main__":
    main() 