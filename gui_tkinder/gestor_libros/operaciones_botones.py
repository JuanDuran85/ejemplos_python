"""_summary_

    Gestor de libros con Tkinder y SQLite

"""

from tkinter import END, Listbox, Tk, messagebox
from operaciones_db import crear_tabla, insertar, borrar, visualizar, buscar, actualizar

def comando_visualizar(lista_libro: Listbox) -> None:
    lista_libro.delete(0,END)
    libros: list = visualizar()
    for libro in libros:
        lista_libro.insert(END,libro)
        
def comando_buscar(lista_libro: Listbox, titulo: str, autor: str, anio: int, isbn: int) -> None:
    if titulo or autor or anio or isbn:        
        lista_libro.delete(0,END)
        libros: list = buscar(titulo, autor, anio, isbn)
        for libro in libros:
            lista_libro.insert(END, libro)
    else:
        messagebox.showinfo("Error", "Debes rellenar al menos un campo para poder buscar")

def comando_insertar(titulo: str, autor: str, anio: int, isbn: int, lista_libro: Listbox) -> None:
    if titulo and autor and anio and isbn:
        insertar(titulo, autor, anio, isbn)
        lista_libro.delete(0,END)
        lista_libro.insert(END, (str(titulo), str(autor), anio, isbn))
    else:
        messagebox.showinfo("Error", "Debes rellenar todos los campos para poder insertar")
        
def comando_actualizar(titulo: str, autor: str, anio: int, isbn: int, id: int, lista_libro: Listbox) -> None:
    print(titulo, autor, anio, isbn, id)
    if titulo and autor and anio and isbn and id>=0:
        actualizar(id, titulo, autor, anio, isbn)
        lista_libro.delete(0,END)
        lista_libro.insert(END, "Libro actualizado correctamente")
    else:
       messagebox.showinfo("Error", "Debes rellenar todos los campos para poder actualizar") 
        
def comando_borrar(id: int, lista_libro: Listbox) -> None:
    print(id)
    if id>=0:
        borrar(id)
        lista_libro.delete(0,END)
        lista_libro.insert(END, "Libro borrado correctamente")
    else:
        messagebox.showinfo("Error", "Debes seleccionar un libro para poder borrar")
        
def comando_cerrar(ventana: Tk) -> None:
    messagebox.showinfo("Cerrar", "Cerrando aplicación")
    ventana.destroy()
    exit()