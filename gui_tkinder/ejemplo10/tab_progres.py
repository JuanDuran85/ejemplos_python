import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Tabuladores")
        self.crear_tab()
        
    def crear_tab(self):
        control_tabulador = ttk.Notebook(self)
        tabulador_uno = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador_uno, text="Tab 1")
        control_tabulador.pack(expand=1, fill="both")
        self.crear_componentes_tabulador_uno(tabulador_uno)
        tabulador_dos = ttk.LabelFrame(control_tabulador, text="Contenido")
        control_tabulador.add(tabulador_dos, text="Tab 2")
        self.crear_componentes_tabulador_dos(tabulador_dos)
        
        tabulador_tres = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador_tres, text="Tab 3")
        self.crear_componentes_tabulador_tres(tabulador_tres)
        
        tabulador_cuatro = ttk.LabelFrame(control_tabulador, text="Imagen")
        control_tabulador.add(tabulador_cuatro, text="Tab 4")
        self.crear_componentes_tabulador_cuatro(tabulador_cuatro)
        
        tabulador_quinto = ttk.LabelFrame(control_tabulador, text="Progress Bar")
        control_tabulador.add(tabulador_quinto, text="Tab 5")
        self.crear_componentes_tabulador_cinco(tabulador_quinto)
        
    def crear_componentes_tabulador_uno(self, tabulador_uno):
        etiqueta_uno = ttk.Label(tabulador_uno, text="Etiqueta 1")
        etiqueta_uno.grid(column=0, row=0, sticky=tk.E)
        entrada_uno = ttk.Entry(tabulador_uno, width=20)
        entrada_uno.grid(row=0, column=0, padx=5, pady=5)
        def enviar_metodo():
            messagebox.showinfo("Mensaje", "Hola " + entrada_uno.get())
        boton_uno = ttk.Button(tabulador_uno, text="Boton 1", command=enviar_metodo)
        boton_uno.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
        
    def crear_componentes_tabulador_dos(self,tabulador_dos):
        contenido = "Este es el texto en el contenido. }Dolore labore non enim magna deserunt. Ullamco incididunt cupidatat ex do veniam mollit dolor tempor tempor et. Laborum mollit cillum irure magna voluptate anim amet fugiat sit eiusmod officia officia. Consectetur reprehenderit aute fugiat incididunt sunt commodo consectetur Lorem anim aute reprehenderit ea consectetur cupidatat. Pariatur duis magna pariatur consectetur anim anim ea do elit cupidatat amet consequat. Culpa ea sint ipsum dolor do laborum. Nisi minim nostrud laboris adipisicing aliquip pariatur sunt et excepteur et culpa consectetur. Este es el texto en el contenido. }Dolore labore non enim magna deserunt. Ullamco incididunt cupidatat ex do veniam mollit dolor tempor tempor et. Laborum mollit cillum irure magna voluptate anim amet fugiat sit eiusmod officia officia. Consectetur reprehenderit aute fugiat incididunt sunt commodo consectetur Lorem anim aute reprehenderit ea consectetur cupidatat. Pariatur duis magna pariatur consectetur anim anim ea do elit cupidatat amet consequat. Culpa ea sint ipsum dolor do laborum. Nisi minim nostrud laboris adipisicing aliquip pariatur sunt et excepteur et culpa consectetur."
        scroll = scrolledtext.ScrolledText(tabulador_dos, width=40, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        scroll.grid(row=0, column=0, padx=5, pady=5)

    def crear_componentes_tabulador_tres(self,tabulador_tres):
        datos = [x+1 for x in range(10)]
        combo_box = ttk.Combobox(tabulador_tres, width=15 , values=datos)
        combo_box.grid(row=0, column=0, padx=5, pady=5)
        combo_box.current(0)
        boton_dos = ttk.Button(tabulador_tres, text="Boton 2", command=lambda: messagebox.showinfo("Mensaje", "Seleccionaste: " + combo_box.get()))
        boton_dos.grid(row=1, column=0, padx=5, pady=5)
        
    def crear_componentes_tabulador_cuatro(self,tabulador_cuatro):
        imagen = tk.PhotoImage(file="gui_tkinder/ejemplo9/python.png")
        boton_imagen = ttk.Button(tabulador_cuatro, image=imagen,command=lambda: messagebox.showinfo("Mas info de la imagen", f"Nombre de la imagen: {imagen.name}\nAncho: {imagen.width()}\nAlto: {imagen.height()}"))
        boton_imagen.grid(row=0, column=0, padx=5, pady=5)
        
    def crear_componentes_tabulador_cinco(self,tabulador_cinco):
        barra_progreso = ttk.Progressbar(tabulador_cinco, orient='horizontal',length=350, mode='determinate')
        barra_progreso.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                sleep(0.05)
                barra_progreso['value'] = valor
                barra_progreso.update()
            barra_progreso['value'] = 0
            
        boton_ejecutar = ttk.Button(tabulador_cinco, text="Ejecutar", command=ejecutar_barra)
        boton_ejecutar.grid(row=3, column=0, padx=5, pady=5)
        boton_inicio = ttk.Button(tabulador_cinco, text="Inicio de Progreso", command=lambda: barra_progreso.start())
        boton_inicio.grid(row=1, column=0, padx=5, pady=5)
        boton_ciclo = ttk.Button(tabulador_cinco, text="Ciclo de Progreso", command=lambda: barra_progreso.step())
        boton_ciclo.grid(row=1, column=1, padx=5, pady=5)
        boton_fin_reinicio = ttk.Button(tabulador_cinco, text="Fin de Progreso", command=lambda: barra_progreso.stop())
        boton_fin_reinicio.grid(row=1, column=2, padx=5, pady=5)
        boton_detener_despues = ttk.Button(tabulador_cinco, text="Detener despues de 5 segundos", command=lambda: barra_progreso.after(5000, barra_progreso.stop))
        boton_detener_despues.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

if __name__ == "__main__":
    window = Window()
    window.mainloop()  