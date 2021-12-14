import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Ejemplo 3")

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# definicion de eventos

def evento_uno():
    print("Evento 1")

def evento_dos():
    print("Evento 2")    

def evento_tres():
    print("Evento 3")
    
def evento_cuatro():
    print("Evento 4")
    boton4.config(text="Evento 4 Activo", fg='blue', relief=tk.GROOVE, bg='yellow')

boton1 = ttk.Button(ventana, text="Boton 1", command=evento_uno)
boton1.grid(row=0, column=0, sticky="nsew", padx=40, pady=40, ipady=40, ipadx=40, columnspan=2)

boton2 = ttk.Button(ventana, text="Boton 2", command=evento_dos)
boton2.grid(row=1, column=0, sticky="nsew")

''' boton3 = ttk.Button(ventana, text="Boton 3", command=evento_tres)
boton3.grid(row=0, column=1, sticky="nsew") '''

boton4 = tk.Button(ventana, text="Boton 4", command=evento_cuatro)
boton4.grid(row=1, column=1, sticky="nsew")

ventana.mainloop()