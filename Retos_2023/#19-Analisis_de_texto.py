"""
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras. OK
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto). OK
 * - Encuentre la palabra más larga. OK
 *
 * Todo esto utilizando un único bucle.
 */
"""

from pathlib import Path

p = Path(__file__).with_name('Texto.txt')

def words():
    print("Texto a analizar")
     
    #Abrir y leer el texto
    document_text = p.open('r',encoding='utf-8')
    text_string = document_text.read()
    print(text_string)
    
    #Se cuentan las frases antes del tragamiento del texto
    phrases = text_string.count('.')
    
    #Se eliminan las comas y los puntos para poder contar la longitud de las palabras
    text_used = text_string.replace(',','')
    text_used = text_used.replace('.','')
    
    #Se cuentan el número total de palabras
    total_words = len(text_used.split())
    
    
    large = text_used.split()
    size = 0
    word = ""
    total_size = 0
    for n in large:
        word_size = len(n)
        if word_size > int(size):
            size = len(n)
            word = n
        total_size += len(n)
            
        
    print(f"Número de oraciones del texto:{phrases}")
    print(f"La longitud media de las palabras es:{round(total_size/total_words)}")
    print(f"Número total de palabras:{total_words}")
    print(f"La palabra mas larga es:{word} con {size} letras")
    
def main():
    words()
    
if __name__ == "__main__":
    main() 