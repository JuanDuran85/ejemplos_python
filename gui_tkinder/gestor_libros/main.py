"""_summary_

    Gestor de libros con Tkinder y SQLite

"""

from operaciones_botones import comando_actualizar, comando_borrar, comando_buscar, comando_cerrar, comando_insertar, comando_visualizar
from tkinter import END, Listbox, Scrollbar, StringVar, Tk, Button, Entry, Label

# funciones especiales
def seleccion_fila(event: object) -> None:
    global indice_libro_db
    try:
        selection = event.widget.curselection()
        if selection[0] >= 0:
            indice_fila = selection[0]
            fila_seleccionada: tuple = event.widget.get(indice_fila)
            indice_libro_db = int(fila_seleccionada[0])
            entrada_titulo.delete(0,END)
            entrada_titulo.insert(END,fila_seleccionada[1])
            entrada_autor.delete(0,END)
            entrada_autor.insert(END,fila_seleccionada[2])
            entrada_anio.delete(0,END)
            entrada_anio.insert(END,fila_seleccionada[3])
            entrada_isbn.delete(0,END)
            entrada_isbn.insert(END,fila_seleccionada[4])
    except Exception as e:
        print(f"Error en evento seleccion fila: {e}")

ventana: Tk = Tk()
ventana.title("Gestor de libros")

# creando etiquetas
etiqueta_uno: Label = Label(ventana, text="Titulo")
etiqueta_uno.grid(row=0, column=0, padx=10, pady=10)

etiqueta_dos: Label = Label(ventana, text="Autor")
etiqueta_dos.grid(row=0, column=2, padx=10, pady=10)

etiqueta_tres: Label = Label(ventana, text="Año")
etiqueta_tres.grid(row=1, column=0, padx=10, pady=10)

etiqueta_cuatro: Label = Label(ventana, text="ISBN")
etiqueta_cuatro.grid(row=1, column=2, padx=10, pady=10)

# entrada de datos
titulo_libro: StringVar = StringVar()
entrada_titulo: Entry = Entry(ventana, textvariable=titulo_libro)
entrada_titulo.grid(row=0, column=1, padx=10, pady=10)

autor_libro: StringVar = StringVar()
entrada_autor: Entry = Entry(ventana, textvariable=autor_libro)
entrada_autor.grid(row=0, column=3, padx=10, pady=10)

anio_libro: StringVar = StringVar()
entrada_anio: Entry = Entry(ventana, textvariable=anio_libro)
entrada_anio.grid(row=1, column=1, padx=10, pady=10)

isbn_libro: StringVar = StringVar()
entrada_isbn: Entry = Entry(ventana, textvariable=isbn_libro)
entrada_isbn.grid(row=1, column=3, padx=10, pady=10)

# lista de libros y scrollbar
lista_libro: Listbox = Listbox(ventana, height=15, width=28, borderwidth=5, relief="groove")
lista_libro.grid(row=2, column=0, rowspan=8, columnspan=2)

scrollbar_libros: Scrollbar = Scrollbar(ventana)
scrollbar_libros.grid(row=2, column=2, rowspan=6)

lista_libro.configure(yscrollcommand=scrollbar_libros.set)
scrollbar_libros.configure(command=lista_libro.yview)

# incluyendo evento a la lista
lista_libro.bind("<<ListboxSelect>>",seleccion_fila)

# botones
boton_visualizar: Button = Button(ventana, text="Visualizar", width=12, command= lambda: comando_visualizar(lista_libro)).grid(row=2, column=3, padx=10, pady=10)

boton_buscar: Button = Button(ventana, text="Buscar", width=12, command= lambda: comando_buscar(lista_libro, titulo_libro.get(), autor_libro.get(), anio_libro.get(), isbn_libro.get())).grid(row=3, column=3, padx=10, pady=10)

boton_anadir: Button = Button(ventana, text="Añadir", width=12, command= lambda: comando_insertar(titulo_libro.get(), autor_libro.get(), anio_libro.get(), isbn_libro.get(), lista_libro)).grid(row=4, column=3, padx=10, pady=10)

boton_actualizar: Button = Button(ventana, text="Actualizar", width=12, command= lambda: comando_actualizar(titulo_libro.get(), autor_libro.get(), anio_libro.get(), isbn_libro.get(), indice_libro_db, lista_libro)).grid(row=5, column=3, padx=10, pady=10)

boton_borrar: Button = Button(ventana, text="Borrar", width=12, command= lambda: comando_borrar(indice_libro_db, lista_libro)).grid(row=6, column=3, padx=10, pady=10)

boton_cerrar: Button = Button(ventana, text="Cerrar", width=12, command= lambda: comando_cerrar(ventana)).grid(row=7, column=3, padx=10, pady=10)

ventana.mainloop()