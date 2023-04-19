"""/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */
"""


# Import the tkinter module
from tkinter import messagebox, ttk
from tkinter.messagebox import showinfo
import tkinter as tk
 
# Creating the GUI window.
window = tk.Tk()
window.title("Aurebesh Translator")
window.geometry("400x150")

# Labels
w = tk.Label(window, text="Aurebesh Translator")
w.grid(row=0,column=6)

selected_languaje_A = tk.StringVar()

comboA = ttk.Combobox(state="readonly",
    values=["Aurebesh", "Castellano"],textvariable=selected_languaje_A
    )
comboA.grid(row=6,column=4,padx=10)
#comboA.current(0)

def set_lenguaje(event):
    
    lenguaje = selected_languaje_A.get()
    if lenguaje == "Castellano":
        result_text.config(font="Times")
        result_text.config(width=30)
        result_text.grid(row=6,column=6,padx=10)
    else:
        result_text.config(font="Aurebesh")
        result_text.config(width=30)
        result_text.grid(row=6,column=6,padx=10)
    

comboA.bind('<<ComboboxSelected>>', lambda _: set_lenguaje(selected_languaje_A.get()))

result_text = tk.Entry(window,width=30)
result_text.grid(row=6,column=6,padx=10)

 
window.mainloop()