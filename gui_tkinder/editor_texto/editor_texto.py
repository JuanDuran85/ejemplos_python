import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfilename


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.FRESE = "Editor de texto"
        self.title(self.FRESE)
        # configuracion del tamaño minimo de la ventana
        self.rowconfigure(0, minsize=600, weight=1)
        # configuracion minima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo de campo de texto
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        # Atributo de archivo
        self.archivo = None
        # Atributo para saber si ya se abrio un archivo anteriormente
        self.archivo_abierto = False
        # crear componentes
        self._crear_widget()
        # crear menu
        self.crear_menu()

    def _crear_widget(self):
        frames_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        tk.Button(frames_botones, text="Abrir", command=self._abrir_archivo).grid(
            row=0, column=0, sticky="we", padx=5, pady=5
        )
        tk.Button(frames_botones, text="Guardar", command=self._guardar_archivo).grid(
            row=1, column=0, sticky="we", padx=5, pady=5
        )
        tk.Button(frames_botones, text="Guardar como", command=self._guardar_como).grid(
            row=2, column=0, sticky="we", padx=5, pady=5
        )
        # se coloca el frama de manera vertical
        frames_botones.grid(row=0, column=0, sticky="ns")
        # agregar el campo de texto, expandiendo por completo el espacio disponible
        self.campo_texto.grid(row=0, column=1, sticky="nswe")

    def crear_menu(self):
        # creamos el menu de la app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        # se agregan las opciones al menu
        # menu archivo con tearoff para que el menu no se separe
        menu_archivo = tk.Menu(menu_app, tearoff=0)
        menu_app.add_cascade(label="Archivo", menu=menu_archivo)
        # agregando opciones del menu de archivo
        menu_archivo.add_command(label="Abrir", command=self._abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self._guardar_archivo)
        menu_archivo.add_command(label="Guardar como...", command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.quit)

    def _abrir_archivo(self):
        # se abre el archivo pars edicion
        self.archivo_abierto = askopenfile(mode="r+")
        print(self.archivo_abierto)
        # eliminamos el texto anterior en la caja de texto
        self.campo_texto.delete(1.0, tk.END)
        # se verifica si hay un archivo abierto
        if not self.archivo_abierto:
            messagebox.showerror("Error", "No se pudo abrir el archivo")
            return
        # abrimos el archivo en modo lectura escritura como un recuerso
        with open(self.archivo_abierto.name, "r+") as self.archivo:
            try:
                # leer el contenido del archivo abierto
                texto = self.archivo.read()
                # insertar el contenido en la caja de texto
                self.campo_texto.insert(1.0, texto)
                # modificamos el titulo de la aplicacion
                self.title(f"*Editor Texto - {self.archivo_abierto.name}")
            except Exception as e:
                print(e)
                messagebox.showerror(
                    "Error", f"No se pudo abrir el archivo {self.archivo_abierto.name}"
                )
                self.archivo.close()
                self.archivo_abierto = False
                self.title(self.FRESE)
                self.campo_texto.delete(1.0, tk.END)

    def _guardar_archivo(self):
        # si ya se abrio un archivo anteriormente se sobreescribe
        if self.archivo_abierto:
            # salvamos el archivo y se abre en modo escritura
            with open(self.archivo_abierto.name, "w") as self.archivo:
                try:
                    # leemos el texto de la caja de texto
                    texto = self.campo_texto.get(1.0, tk.END)
                    # escribimos el contenido al mismo archivo
                    self.archivo.write(texto)
                    # cambiamos el titulo de la app
                    self.title(f"Editor Texto - {self.archivo_abierto.name}")
                except Exception as e:
                    print(e)
                    messagebox.showerror(
                        "Error",
                        f"No se pudo guardar el archivo {self.archivo_abierto.name}",
                    )
                    self.archivo.close()
                    self.archivo_abierto = False
                    self.title(self.FRESE)
                    self.campo_texto.delete(1.0, tk.END)
        else:
            self._guardar_como()

    def _guardar_como(self):
        # salvamos el archivo actual como un nuevo archivo en la pc
        self.archivo = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivo de Texto", "*.txt"), ("Todos los archivos", "*.*")],
        )

        if not self.archivo:
            messagebox.showerror("Error", "No se pudo guardar el archivo")
            return
        # abrimos el archivo en modo escritura
        with open(self.archivo, "w") as self.archivo:
            try:
                texto = self.campo_texto.get(1.0, tk.END)
                # escribimos el contenido al nuevo archivo
                self.archivo.write(texto)
                # cambiamos el nombre del archivo
                self.title(f"Editor Texto - {self.archivo.name}")
                # se indica que ya se abrio un archivo
                self.archivo_abierto = self.archivo
            except Exception as e:
                print(e)
                messagebox.showerror("Error", "No se pudo guardar el archivo")
                self.archivo.close()
                self.archivo_abierto = False
                self.title(self.FRESE)
                self.campo_texto.delete(1.0, tk.END)


if __name__ == "__main__":
    editor = Editor()
    editor.mainloop()
