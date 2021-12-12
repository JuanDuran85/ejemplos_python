import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Ejemplo 2")

# definicion de metodos de los eventos
def evento_uno():
    print("Evento 1")
    boton1.config(text="Evento 1 del boton 1")

def evento_dos():
    print("Evento 2")
    boton2.config(text="Evento 2 del boton 2")

# N(arriba), E(derecha), S(abajo), W(izquierda)
# definimos dos botones
boton1 = ttk.Button(ventana, text="Boton 1", command=evento_uno)
boton1.grid(row=0, column=0, sticky="W")

boton2 = ttk.Button(ventana, text="Boton 2",command=evento_dos)
boton2.grid(row=1, column=0,sticky='E')

ventana.mainloop()