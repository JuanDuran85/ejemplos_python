import tkinter as tk
from tkinter import ttk

''' ------------------- Metodos ------------------- '''
def metodo_enviar():
    print('Enviar')
    print(entrada_uno.get())
    print(entrada_dos.get())
    print(entrada_tres.get())
    print(entrada_cuatro.get())
    boton_uno.config(text=entrada_uno.get())
    # seleccionar el texto de la caja
    entrada_dos.select_range(0, tk.END)
    # eliminar escrito de la caja
    entrada_uno.delete(0,tk.END)
''' ----------------------------------------------- '''

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Ejemplo 3")

entrada_uno = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada_uno.grid(column=0, row=0)
entrada_uno.insert(0, "Escriba su nombre")
entrada_uno.insert(tk.END, '.')

entrada_dos = ttk.Entry(ventana, width=30, justify=tk.CENTER, show="*")
entrada_dos.grid(column=0, row=1)
entrada_dos.insert(0,"Escriba la contraseña")
entrada_dos.insert(tk.END, '.')

entrada_tres = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.DISABLED)
entrada_tres.grid(column=0, row=2)
entrada_tres.insert(0,"Caja deshabilitada")

entrada_cuatro = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada_cuatro.grid(column=0, row=3)
entrada_cuatro.insert(0,"Caja habilitada Solo lectura")
entrada_cuatro.config(state = "readonly")

# creando variable

entrada_cinco = ttk.Entry(ventana, width=30,)

# lecutra de la entrada en las cajas de texto
boton_uno = ttk.Button(ventana, text="Enviar", command=metodo_enviar)
boton_uno.grid(column=0, row=4)

ventana.mainloop()