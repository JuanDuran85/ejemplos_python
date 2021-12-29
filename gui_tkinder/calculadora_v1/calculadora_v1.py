import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x370")
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
        entrada_frame.pack()
        #componente de caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18), textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=5)
        
        #agregar el segundo frama para la parte inferior de la calculadora
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()
        
        # Primer renglon de botones
        # boton para limpiar
        tk.Button(botones_frame, text='C', width='34', height=3, bd=0, bg='#eee', cursor='hand2',command=self._evento_limpiar).grid(row=0, column=0, columnspan=3, pady=1, padx=1)
        
        # boton para dividir
        tk.Button(botones_frame, text='/', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: self._evento_click('/')).grid(row=0, column=3, pady=1, padx=1)
        
        # Segundo renglon de botones
        #boton numero 7
        tk.Button(botones_frame, text='7', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('7')).grid(row=1, column=0, pady=1, padx=1)
        #boton numero 8
        tk.Button(botones_frame, text='8', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('8')).grid(row=1, column=1, pady=1, padx=1)
        #boton numero 9
        tk.Button(botones_frame, text='9', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('9')).grid(row=1, column=2, pady=1, padx=1)
        #boton *
        tk.Button(botones_frame, text='*', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: self._evento_click('*')).grid(row=1, column=3, pady=1, padx=1)
        
        # Tercer renglon de botones
        # boton numero 4
        tk.Button(botones_frame, text='4', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('4')).grid(row=2, column=0, pady=1, padx=1)
        # boton numero 5
        tk.Button(botones_frame, text='5', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('5')).grid(row=2, column=1, pady=1, padx=1)
        #boton numero 6
        tk.Button(botones_frame, text='6', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('6')).grid(row=2, column=2, pady=1, padx=1)
        # boton -
        tk.Button(botones_frame, text='-', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: self._evento_click('-')).grid(row=2, column=3, pady=1, padx=1)
        
        
        # Cuarto renglon de botones
        # boton numero 1
        tk.Button(botones_frame, text='1', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('1')).grid(row=3, column=0, pady=1, padx=1)
        # boton numero 2
        tk.Button(botones_frame, text='2', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('2')).grid(row=3, column=1, pady=1, padx=1)
        # boton numero 3
        tk.Button(botones_frame, text='3', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('3')).grid(row=3, column=2, pady=1, padx=1)
        # boton +
        tk.Button(botones_frame, text='+', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= lambda: self._evento_click('+')).grid(row=3, column=3, pady=1, padx=1)
        
        # Quinto renglon de botones
        # boton numero 0
        tk.Button(botones_frame, text='0', width=22, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('0')).grid(row=4, column=0, columnspan=2, pady=1, padx=1)
        # boton punto .
        tk.Button(botones_frame, text='.', width=9, height=3, bd=0, bg='#fff', cursor='hand2', command= lambda: self._evento_click('.')).grid(row=4, column=2, pady=1, padx=1)
        # boton igual =
        tk.Button(botones_frame, text='=', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command= self._evento_igual).grid(row=4, column=3, pady=1, padx=1)
        
    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)
    
    def _evento_click(self,operations):
        self.expresion += operations
        self.entrada_texto.set(self.expresion)
    
    def _evento_igual(self):
        try:
            if self.expresion:
                resultado = eval(self.expresion)
                self.entrada_texto.set(str(resultado))
        except Exception as e:
            messagebox.showerror('Error', f'Error en la expresion: {e}')
            self.entrada_texto.set(str(e))
        finally:
            self.expresion = ''
        
if __name__ == '__main__':
    app = Calculadora()
    app.mainloop()