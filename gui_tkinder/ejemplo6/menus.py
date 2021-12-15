import sys
import tkinter as tk
from tkinter import Menu, ttk, messagebox

def exit_event():
    if messagebox.askokcancel("Salir", "¿Desea salir?"):
        window.quit()
        window.destroy()
        sys.exit()

def crear_menu():
    #configurar el menu principal
    menu_principal = Menu(window)
    # propiedad tearoff se configura a falso para que no se separe el menu de la interface
    menu_archivo = Menu(menu_principal, tearoff = 0)
    # Agregar una nueva opcion al menu de archivo
    menu_archivo.add_command(label = "Nuevo")
    # agregando separador
    menu_archivo.add_separator()
    # Agregar una nueva opcion al menu de archivo
    menu_archivo.add_command(label = "Salir", command = exit_event)
    # creando submenu de ayuda
    submenu_ayuda = Menu(menu_principal, tearoff = 0)
    # Agregar una nueva opcion al menu de archivo
    submenu_ayuda.add_command(label = "Acerca de...")
    # agregando al menu principal el nuevo sub menu
    menu_principal.add_cascade(label = "Ayuda", menu = submenu_ayuda)
    # agregar el sub menu al menu principal
    menu_principal.add_cascade(label = "Archivo", menu = menu_archivo)
    # mostrar el menu en la ventana principal
    window.config(menu = menu_principal)

window = tk.Tk()
window.geometry("600x400")
window.title("Menus")

box_one = ttk.Entry(window, width = 30, justify = tk.CENTER)
box_one.grid(column = 0, row = 1)

btn_one = ttk.Button(window, text = "Enviar")
btn_one.grid(column = 1, row = 1)

crear_menu()

window.mainloop()