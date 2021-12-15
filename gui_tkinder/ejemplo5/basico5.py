import tkinter as tk
from tkinter import ttk, messagebox

''' Definiendo metodos '''
def event_btn_two():
    messagebox.showwarning(title="Alerta", message= box_text_two.get() if box_text_two.get() else "No hay texto")
    # messagebox.showerror(title="Titulo", message="Mensaje")
    
def event_btn_three():
    if box_text_three.get():
        messagebox.showinfo(title="Informacion", message=box_text_three.get())
    else:
        messagebox.showwarning(title="Alerta", message="No hay texto")

''' Creando una ventana '''
window_principal = tk.Tk()
window_principal.geometry("600x400")
window_principal.title("Ejemplo 5")

''' Creando una caja de texto '''
box_text_one = ttk.Entry(window_principal, width=30, justify=tk.CENTER)
box_text_one.grid(column=0, row=0)

box_text_two = ttk.Entry(window_principal, width=30, justify=tk.CENTER)
box_text_two.grid(column=0, row=1)

box_text_three = ttk.Entry(window_principal, width=30, justify=tk.CENTER)
box_text_three.grid(column=0, row=2)

''' Creando un boton '''
button_one = ttk.Button(window_principal, text="Enviar Uno", command=lambda: messagebox.showinfo("Informacion", box_text_one.get()))
button_one.grid(column=1, row=0)

button_two = ttk.Button(window_principal, text="Enviar Dos", command=event_btn_two)
button_two.grid(column=1, row=1)

button_three = ttk.Button(window_principal, text="Enviar Tres", command=event_btn_three)
button_three.grid(column=1, row=2)

''' Levantando la ventana '''
window_principal.mainloop()