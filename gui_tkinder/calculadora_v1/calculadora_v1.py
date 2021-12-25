import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x450")
        self.resizable(False, False)
        self.title("Calculadora")
        self.iconbitmap("@/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/calculadora_v1/icono.xbm")
        
        # Atributos de clase
        self.expresion = ''
        # caja de texto (input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # crear metodo para componentes
        self._creacion_componentes()
    
    #Metodos de clase
    # metodo para crear componente    
    def _creacion_componentes(self):
        # creando un primer frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP, fill=tk.X)
        #componente de caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18), textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=5)
        
        #agregar el segundo frama para la parte inferior de la calculadora
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack(side=tk.TOP, fill=tk.X)
        

if __name__ == '__main__':
    app = Calculadora()
    app.mainloop()