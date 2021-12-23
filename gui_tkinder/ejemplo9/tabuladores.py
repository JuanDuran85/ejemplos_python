import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

window = tk.Tk()
window.title("Tabuladores")
window.geometry("400x400")

def crear_componentes_tabulador_uno(tabulador_uno):
    # agregamos una etiqueta
    etiqueta_uno = ttk.Label(tabulador_uno, text="Etiqueta 1")
    etiqueta_uno.grid(column=0, row=0, sticky=tk.E)
    #agregar etiquetas y componente de entrada
    entrada_uno = ttk.Entry(tabulador_uno, width=20)
    entrada_uno.grid(row=0, column=0, padx=5, pady=5)
    # agregando un boton
    def enviar_metodo():
        messagebox.showinfo("Mensaje", "Hola " + entrada_uno.get())
    boton_uno = ttk.Button(tabulador_uno, text="Boton 1", command=enviar_metodo)
    boton_uno.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

def crear_componentes_tabulador_dos(tabulador_dos):
    contenido = "Este es el texto en el contenido. }Dolore labore non enim magna deserunt. Ullamco incididunt cupidatat ex do veniam mollit dolor tempor tempor et. Laborum mollit cillum irure magna voluptate anim amet fugiat sit eiusmod officia officia. Consectetur reprehenderit aute fugiat incididunt sunt commodo consectetur Lorem anim aute reprehenderit ea consectetur cupidatat. Pariatur duis magna pariatur consectetur anim anim ea do elit cupidatat amet consequat. Culpa ea sint ipsum dolor do laborum. Nisi minim nostrud laboris adipisicing aliquip pariatur sunt et excepteur et culpa consectetur. Este es el texto en el contenido. }Dolore labore non enim magna deserunt. Ullamco incididunt cupidatat ex do veniam mollit dolor tempor tempor et. Laborum mollit cillum irure magna voluptate anim amet fugiat sit eiusmod officia officia. Consectetur reprehenderit aute fugiat incididunt sunt commodo consectetur Lorem anim aute reprehenderit ea consectetur cupidatat. Pariatur duis magna pariatur consectetur anim anim ea do elit cupidatat amet consequat. Culpa ea sint ipsum dolor do laborum. Nisi minim nostrud laboris adipisicing aliquip pariatur sunt et excepteur et culpa consectetur."
    # creamos un componente scroll
    scroll = scrolledtext.ScrolledText(tabulador_dos, width=40, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    # mostramos el componente scroll
    scroll.grid(row=0, column=0, padx=5, pady=5)

def crear_componentes_tabulador_tres(tabulador_tres):
    # creamos una lista usando data list comprehensions
    datos = [x+1 for x in range(10)]
    combo_box = ttk.Combobox(tabulador_tres, width=15 , values=datos)
    combo_box.grid(row=0, column=0, padx=5, pady=5)
    # seleccionamos un elemento por defecto a mostrar
    combo_box.current(0)
    # agregar un boton para saber cual fue la opcion seleccionada
    boton_dos = ttk.Button(tabulador_tres, text="Boton 2", command=lambda: messagebox.showinfo("Mensaje", "Seleccionaste: " + combo_box.get()))
    boton_dos.grid(row=1, column=0, padx=5, pady=5)
    
def crear_componentes_tabulador_cuatro(tabulador_cuatro):
    # trabajando con imagenes en tkinder
    imagen = tk.PhotoImage(file="gui_tkinder/ejemplo9/python.png")
    boton_imagen = ttk.Button(tabulador_cuatro, image=imagen,command=lambda: messagebox.showinfo("Mas info de la imagen", f"Nombre de la imagen: {imagen.name}\nAncho: {imagen.width()}\nAlto: {imagen.height()}"))
    boton_imagen.grid(row=0, column=0, padx=5, pady=5)
    
def crear_componentes_tabulador_cinco(tabulador_cinco):
    # trabajando con barra de progreso
    # creamos el componente de barra de progreso
    barra_progreso = ttk.Progressbar(tabulador_cinco, orient='horizontal',length=350, mode='determinate')
    barra_progreso.grid(row=0, column=0, padx=5, pady=5, columnspan=4)
    def ejecutar_barra():
        barra_progreso['maximum'] = 100
        for valor in range(101):
            # se activa un tiempo muerto de espera
            sleep(0.05)
            # incremetamos nuestra barra de progreso
            barra_progreso['value'] = valor
            # actualizamos la barra de progreso
            barra_progreso.update()
        barra_progreso['value'] = 0
            
    # botones para controlar los eventos de la barra de progreso
    boton_ejecutar = ttk.Button(tabulador_cinco, text="Ejecutar", command=ejecutar_barra)
    boton_ejecutar.grid(row=3, column=0, padx=5, pady=5)
    boton_inicio = ttk.Button(tabulador_cinco, text="Inicio de Progreso", command=lambda: barra_progreso.start())
    boton_inicio.grid(row=1, column=0, padx=5, pady=5)
    boton_ciclo = ttk.Button(tabulador_cinco, text="Ciclo de Progreso", command=lambda: barra_progreso.step())
    boton_ciclo.grid(row=1, column=1, padx=5, pady=5)
    boton_fin_reinicio = ttk.Button(tabulador_cinco, text="Fin de Progreso", command=lambda: barra_progreso.stop())
    boton_fin_reinicio.grid(row=1, column=2, padx=5, pady=5)
    # detener la barra despues de ciertos minutos
    boton_detener_despues = ttk.Button(tabulador_cinco, text="Detener despues de 5 segundos", command=lambda: barra_progreso.after(5000, barra_progreso.stop))
    boton_detener_despues.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

def crear_tab():
    # creamos un tab control, para ellos usamos la clase Notebook
    control_tabulador = ttk.Notebook(window)
    # agregar un frame o marco para agregar dentro del tab y organizar
    tabulador_uno = ttk.Frame(control_tabulador)
    # agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador_uno, text="Tab 1")
    #mostramos el tabular para que se muestre
    control_tabulador.pack(expand=1, fill="both")
    crear_componentes_tabulador_uno(tabulador_uno)
    
    # creamos un segundo tabulador al control de tabuladores
    tabulador_dos = ttk.LabelFrame(control_tabulador, text="Contenido")
    control_tabulador.add(tabulador_dos, text="Tab 2")
    crear_componentes_tabulador_dos(tabulador_dos)
    
    # creamos un tercer tabulador
    tabulador_tres = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador_tres, text="Tab 3")
    # cremos los coponentes del tercer tabulador
    crear_componentes_tabulador_tres(tabulador_tres)
    
    # creando un cuarto tabulador
    tabulador_cuatro = ttk.LabelFrame(control_tabulador, text="Imagen")
    control_tabulador.add(tabulador_cuatro, text="Tab 4")
    # creamos los componentes del cuarto tabulador
    crear_componentes_tabulador_cuatro(tabulador_cuatro)
    
    # creando un quinto tabulador
    tabulador_quinto = ttk.LabelFrame(control_tabulador, text="Progress Bar")
    control_tabulador.add(tabulador_quinto, text="Tab 5")
    # creamos los componentes del quinto tabulador
    crear_componentes_tabulador_cinco(tabulador_quinto)
    
crear_tab()

window.mainloop()
