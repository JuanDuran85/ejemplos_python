import tkinter as tk

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de texto")
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
        
    def _crear_widget(self):
        frames_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        tk.Button(frames_botones, text="Abrir", command=self._abrir_archivo).grid(row=0, column=0, sticky='we', padx=5, pady=5)
        tk.Button(frames_botones, text="Guardar", command=self._guardar_archivo).grid(row=1, column=0, sticky='we', padx=5, pady=5)
        tk.Button(frames_botones, text="Guardar como", command=self._guardar_como).grid(row=2, column=0, sticky='we', padx=5, pady=5)
        # se coloca el frama de manera vertical
        frames_botones.grid(row=0, column=0, sticky='ns')
        # agregar el campo de texto, expandiendo por completo el espacio disponible
        
    def _abrir_archivo(self):
        pass
    
    def _guardar_archivo(self):
        pass
    
    def _guardar_como(self):
        pass
        
if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()