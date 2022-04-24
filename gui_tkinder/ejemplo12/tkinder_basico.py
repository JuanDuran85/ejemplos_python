from tkinter import Button, Entry, Frame, IntVar, Label, Radiobutton, Text, Tk, Checkbutton, filedialog, messagebox

raiz: Tk = Tk()
raiz.title("Ejemplo 12")

# mostrando etiquetas con mensajes
mensaje: Label = Label(raiz, text="Mensaje con Label")
mensaje.config(bg="red", fg="white", font=("Cortana", 30))
mensaje.pack()

# entrada de texto
entrada: Entry = Entry(raiz)
entrada.config(justify="center", show="*", width=30)
entrada.pack()

# creando texto a mostrar
entrada_texto: Text = Text(raiz)
entrada_texto.config(width=20, height=10, font=(
    "Cortana", 14), padx=10, pady=10, fg="green", selectbackground="blue")
entrada_texto.pack()

# creando un boton
boton: Button = Button(
    raiz, text="Boton", command=lambda: entrada_texto.insert(1.0, entrada.get()))
boton.config(fg="blue", bg="yellow", font=("Cortana", 20))
boton.pack()

opcion: IntVar = IntVar()


def seleccionar() -> None:
    print(f"Seleccionaste {opcion.get()}")


# creamos un radio button
radio_button: Radiobutton = Radiobutton(
    raiz, text="Opcion", variable=opcion, value=1, command=seleccionar)
radio_button.pack()
radio_button_dos: Radiobutton = Radiobutton(
    raiz, text="Opcion 2", variable=opcion, value=2, command=seleccionar)
radio_button_dos.pack()
radio_button_tres: Radiobutton = Radiobutton(
    raiz, text="Opcion 3", variable=opcion, value=3, command=seleccionar)
radio_button_tres.pack()

# boton de verificacion o check

check_uno: IntVar = IntVar()


def verificar() -> None:
    valor = check_uno.get()
    if valor:
        print("Activado el check")
        print(f"Valor: {valor} ")
    else:
        print("Desactivado el check")
        print(f"Valor: {valor} ")


check_button: Checkbutton = Checkbutton(
    raiz, text="Verificacion", variable=check_uno, onvalue=1, offvalue=0, command=verificar)
check_button.pack()


# creando y mostrando un popup
boton_dos: Button = Button(raiz, text="Pulsa para visualizar",
                           command=lambda: messagebox.showinfo("Titulo", "Mensaje"))
boton_dos.config(fg="blue", bg="yellow", font=("Cortana", 20))
boton_dos.pack()

# creando y mostrando un popup para preguntas


def pregunta() -> None:
    resultado: str = messagebox.askquestion("Titulo", "Mensaje")
    print(f"El resultado es: {resultado}")
    if resultado == "yes":
        print("Has pulsado si")
    else:
        print("Has pulsado no")


boton_tres: Button = Button(raiz, text="Pulsa para pregunta", command=pregunta)
boton_tres.config(fg="blue", bg="yellow", font=("Cortana", 20))
boton_tres.pack()

# filedialog para abrir fichero si existe


def abrir_fichero() -> None:
    ruta_fichero: str = filedialog.askopenfilename(
        initialdir="/home/juan/Descargas/", title="Selecciona un fichero", filetypes=(("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    print(f"La ruta del fichero es: {ruta_fichero}")


boton_cuatro: Button = Button(
    raiz, text="Pulsa para abrir", command=abrir_fichero)
boton_cuatro.config(fg="blue", bg="yellow", font=("Cortana", 20))
boton_cuatro.pack()

# creando un frame
frame: Frame = Frame(raiz)
frame.config(bg="#f2e050", width=200, height=200)
frame.pack()

raiz.mainloop()
