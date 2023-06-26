"""
/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */
 ↑ ↑ ↓ ↓ ← → ← → B A
"""
import keyboard

konami = ["flecha arriba","flecha arriba","flecha abajo","flecha abajo","flecha izquierda","flecha derecha","flecha izquierda","flecha derecha","b","a"]
codigo_introducido = []
codigo = "\u2191 "+"\u2191 "+"\u2193 "+"\u2193 "+"\u2190 "+"\u2192 "+"\u2190 "+"\u2192 "+"b a"

while len(codigo_introducido) < 10:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        codigo_introducido.append(key)

if konami == codigo_introducido:
    print(codigo)
    print("PIRATA")
else:
    print(codigo_introducido)
    print("Sigue buscando")