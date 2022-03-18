from tkinter import Entry, Frame, Label, Text, Tk

raiz: Tk = Tk()
raiz.title("Ejemplo 12")

# mostrando etiquetas con mensajes 
mensaje: Label = Label(raiz, text="Mensaje con Label")
mensaje.config(bg="red", fg="white", font=("Cortana",30))
mensaje.pack()

# entrada de texto
entrada: Entry = Entry(raiz)
entrada.config(justify="center", show="*", width=30)
entrada.pack()

# creando texto a mostrar
entrada_texto: Text = Text(raiz)
entrada_texto.config(width=20, height=10, font=("Cortana",14), padx=10, pady=10, fg="green", selectbackground="blue")
entrada_texto.pack()

# creando un boton


# creando un frame
frame: Frame = Frame(raiz)
frame.config(bg="#f2e050", width=200, height=200)
frame.pack()

raiz.mainloop()