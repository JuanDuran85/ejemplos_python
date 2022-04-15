"""_summary_

    Interfaz para juego de cartas - Black Jack / 21

"""

from tkinter import Canvas, PhotoImage, Tk, Label, Button, Entry, StringVar, IntVar, END, W, E, N, S, messagebox
from Repartidor import Repartidor
from Jugador import Jugador
from JugadorVirtual import JugadorVirtual

class InterfazJuegoCartas:
    
    def __init__(self,) -> None:
        self.ventana: Tk = Tk()
        self.ventana.geometry("1200x600")
        self.canvas: Canvas = Canvas(self.ventana, width=1200, height=600)
        self.canvas.pack()
        self.dibujar_fondo()
        self.dibujar_etiqutas()
        
        self.boton_iniciar: Button = Button(self.ventana, text="Iniciar Juego", command=self.jugar)
        self.boton_quedarse: Button = Button(self.ventana, text="Quedarse", command=self.finalizar_juego)
        self.boton_solicitar: Button = Button(self.ventana, text="Solicitar", command=self.solicitar_carta)
        self.ocultar_opciones_juego()
        
        self.jugador_uno: Jugador = Jugador('Jugador 1')
        self.jugador_virtual_uno: JugadorVirtual = JugadorVirtual('Computadora 1')
        self.repartidor: Repartidor = Repartidor([self.jugador_uno, self.jugador_virtual_uno])
        
        self.ventana.mainloop()
    
    def solicitar_carta(self) -> None:
        suma: int = self.jugador_uno.solicitar_carta(self.repartidor.mazo)
        if (suma > 21):
            self.finalizar_juego()
        self.dibujar_rectangulo(1,self.jugador_uno_x - 60, 400, 120, 175, 0)
        self.dibujar_carta(self.jugador_uno_x, self.jugador_uno_y, self.jugador_uno.cartas[-1].obtener_nombre_archivo())
        self.jugador_uno_x += 125
    
    def finalizar_juego(self) -> None:
        print("Juego finalizado")
        self.dibujar_rectangulo(1,self.jugador_virtual_inicio-60,self.jugador_virtual_y-88,120,175,0)
        self.dibujar_carta(self.jugador_virtual_inicio,self.jugador_virtual_y,self.jugador_virtual_uno.cartas[0].obtener_nombre_archivo())
        
        ganador_humano = self.repartidor.determinar_ganador()
        if (ganador_humano):
            print("Ganador: Jugador 1")
            self.etiqueta_ganador.config(text="Ganador: Jugador 1")
        else:
            print("Ganador: Computadora 1")
            self.etiqueta_ganador['text'] = "Ganador: Computadora 1"
        self.ocultar_opciones_juego()
        
    def jugar(self) -> None:
        self.etiqueta_ganador.config(text="")
        self.dibujar_fondo()
        self.jugador_virtual_x: int = 110
        self.jugador_virtual_y: int = 143
        self.jugador_uno_x: int = 110
        self.jugador_uno_y: int = 490
        self.jugador_virtual_inicio: int = self.jugador_virtual_x
        
        cartas = self.repartidor.iniciar_juego()
        
        self.jugador_virtual_uno.jugar(self.repartidor.mazo)
        
        self.jugador_virtual_x = self.estado_inicial(cartas['jv'], self.jugador_virtual_x, self.jugador_virtual_y, True)
        self.jugador_uno_x = self.estado_inicial(cartas['j1'], self.jugador_uno_x, self.jugador_uno_y)
        
        self.mostrar_opciones_juego()
        
    def estado_inicial(self, cartas: list, x: int, y: int, ocultar_primera: bool = False) -> int:
        for i in range(len(cartas)):
            self.dibujar_rectangulo(1,x-60,y-88,120,175,5)
            nombre = "/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/juego_21/images/back.png" if ocultar_primera and i == 0 else cartas[i].obtener_nombre_archivo()
            self.dibujar_carta(x,y,nombre)
            x += 125
        return x
    
    def mostrar_opciones_juego(self) -> None:
        self.boton_solicitar.place(x=700, y=500)
        self.boton_quedarse.place(x=700, y=550)
        self.boton_iniciar.place_forget()
        
    def ocultar_opciones_juego(self) -> None:
        self.boton_iniciar.place(x=400, y=300)
        self.boton_quedarse.place_forget()
        self.boton_solicitar.place_forget()
        
    def dibujar_fondo(self) -> None:
        fondo: PhotoImage = PhotoImage(file="/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/juego_21/images/fondo.png")
        imagen: Label = Label(image=fondo)
        imagen.image = fondo
        
        self.canvas.create_image(0, 0, image=fondo, anchor="nw")
        self.canvas.create_image(600, 0, image=fondo, anchor="nw")
        self.canvas.create_image(600, 200, image=fondo, anchor="nw")
        self.canvas.create_image(0, 200, image=fondo, anchor="nw")
        
        adornos: PhotoImage = PhotoImage(file="/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/juego_21/images/adornos.png")
        imagen: Label = Label(image=adornos)
        adornos = adornos.subsample(7)
        imagen.image = adornos
        self.canvas.create_image(980, 460, image=adornos)
    
    def dibujar_poligono(self, x: list, y: list, **args) -> None:
        puntos: list = []
        for i in range(len(x)):
            puntos.append(x[i])
            puntos.append(y[i])
        
        puntos.append(x[0])
        puntos.append(y[0])
        
        return self.canvas.create_polygon(puntos, **args)
    
    def dibujar_rectangulo(self, cantidad: int, x_inicio: int, y_inicio: int, x_tamano: int, y_tamano: int, margen: int = 10) -> None:
        for _ in range(cantidad):
            self.dibujar_poligono([x_inicio, x_inicio+x_tamano, x_inicio+x_tamano, x_inicio],[y_inicio, y_inicio, y_inicio + y_tamano, y_inicio + y_tamano], fill="#FFFFFF", width=2, outline="#000000")
            x_inicio = x_inicio + x_tamano + margen
    
    def dibujar_etiqutas(self) -> None:
        etiqueta_pc: Label = Label(self.ventana, text="Computadora 1", background="green", foreground="white", font=("Arial", 15))
        etiqueta_pc.place(x=50, y=20)
        etiqueta_jugador_uno: Label = Label(self.ventana, text="Jugador 1", background="green", foreground="white", font=("Arial", 15))
        etiqueta_jugador_uno.place(x=50, y=320)
        self.etiqueta_ganador: Label = Label(self.ventana, text="", background="green", foreground="white", font=("Arial", 15))
        self.etiqueta_ganador.place(x=50,y=280)
    
    def dibujar_carta(self, x: int = 110, y: int = 143, imagen: str = '/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/juego_21/images/2_de_corazones.png') -> None:
        imagen_canvas: PhotoImage = PhotoImage(file=imagen)
        imagen_canvas = imagen_canvas.subsample(2)
        imagen_label: Label = Label(image=imagen_canvas)
        imagen_label.image = imagen_canvas
        self.canvas.create_image(x, y, image=imagen_canvas)
        
def main() -> None:
    InterfazJuegoCartas()
    
if __name__ == '__main__':
    main()