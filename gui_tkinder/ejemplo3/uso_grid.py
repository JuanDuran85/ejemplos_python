import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Ejemplo 3")

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

boton1 = ttk.Button(ventana, text="Boton 1")
boton1.grid(row=0, column=0, sticky="nsew")

boton2 = ttk.Button(ventana, text="Boton 2")
boton2.grid(row=1, column=0, sticky="nsew")

boton3 = ttk.Button(ventana, text="Boton 3")
boton3.grid(row=0, column=1, sticky="nsew")

boton4 = ttk.Button(ventana, text="Boton 4")
boton4.grid(row=1, column=1, sticky="nsew")

ventana.mainloop()