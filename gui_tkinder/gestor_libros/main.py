"""_summary_

    Gestor de libros con Tkinder y SQLite

"""

from tkinter import Listbox, Scrollbar, StringVar, Tk, Button, Entry, Frame, IntVar, Label, Radiobutton, Text, Tk, Checkbutton, filedialog, messagebox

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
lista_libro: Listbox = Listbox(ventana, height=8, width=25)
lista_libro.grid(row=2, column=0, rowspan=6, columnspan=2, padx=10, pady=10)

scrollbar_libros: Scrollbar = Scrollbar(ventana)
scrollbar_libros.grid(row=2, column=2, rowspan=6)

lista_libro.configure(yscrollcommand=scrollbar_libros.set)
scrollbar_libros.configure(command=lista_libro.yview)

ventana.mainloop()
