# GUI - Graphical User Interface

import tkinter as tk
from tkinter import ttk

ICON_ONE_PATH = "gui_tkinder/ejemplo1/equalizer_balance_settings_icon.png"
# creamos un objeto usando la clase tk
ventana = tk.Tk()

# modificando tamaño de la ventana (ancho, alto) con pixeles
ventana.geometry("600x400")

# cambiar el nombre de la ventana
ventana.title("Mi primera ventana")

# cambiar el icono de la ventana
ventana.tk.call('wm', 'iconphoto', ventana._w, tk.PhotoImage(file='gui_tkinder/ejemplo1/equalizer_balance_settings_icon.png'))

# definiendo eventos para el boton
def evento_boton_1():
    print("Entro al evento del boton 1")
    boton1.config(text="Nuevo texto")
    # crear un nuevo componente
    boton2 = ttk.Button(ventana, text="Nuevo boton2")
    boton2.pack()

# creando un boton como componente de la ventana o widget
boton1 = ttk.Button(ventana, text="Boton 1", command=evento_boton_1)

# utilizar el pack layout manager para organizar los widgets y desplegar
boton1.pack()

# iniciar nuestra ventana (solo se ejecuta al final). Si se ejecuta antes no se muestran los cambios
ventana.mainloop()
