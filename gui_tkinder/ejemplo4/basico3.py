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
    
def metodo_enviar_dos():
    # se recupera la informacion a partir de la varinbable asociada con la caja de texto
    boton_dos.config(text=entrada_var_cinco.get())    
    # modificacion mediante la variable y el metodo set
    entrada_var_cinco.set('Nuevo valor')
    # se puede recuperar la informacion por el contenido de la variable o la caja de texto
    print(entrada_var_cinco.get())
    print(entrada_cinco.get())
    # modificar el texto del label
    etiqueta_uno.config(text=entrada_var_cinco.get())
    
''' ----------------------------------------------- '''

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Ejemplo 4")

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

# creando variable para modificar posteriormente con el metodo set y para leer con el metodo get
entrada_var_cinco = tk.StringVar(value="Valor por defecto")
entrada_cinco = ttk.Entry(ventana, width=30, textvariable=entrada_var_cinco)
entrada_cinco.grid(column=0, row=4)

# lecutra de la entrada en las cajas de texto
boton_uno = ttk.Button(ventana, text="Enviar", command=metodo_enviar)
boton_uno.grid(column=0, row=5)

boton_dos = ttk.Button(ventana, text="Enviar Dos", command=metodo_enviar_dos)
boton_dos.grid(column=0, row=6)

# agregando etiqueta o lebel
etiqueta_uno = tk.Label(ventana, text="Aqui se mostrara el texto")
etiqueta_uno.grid(column=0, row=7)


ventana.mainloop()