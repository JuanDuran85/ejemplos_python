"""_summary_

    Interfaz para juego de cartas - Black Jack / 21

"""

from tkinter import Canvas, PhotoImage, Tk, Label, Button, Entry, StringVar, IntVar, END, W, E, N, S, messagebox
from Carta import Carta

class InterfazJuegoCartas:
    
    def __init__(self,) -> None:
        self.ventana: Tk = Tk()
        self.ventana.geometry("1200x600")
        self.canvas: Canvas = Canvas(self.ventana, width=1200, height=600)
        self.canvas.pack()
        self.dibujar_fondo()
        self.dibujar_rectangulo(4, 50, 55, 120, 175, 5)
        carta_uno: Carta = Carta(11,"corazones")
        self.dibujar_carta(110,143,carta_uno.obtener_nombre_archivo())
        self.dibujar_etiqutas()
        self.ventana.mainloop()
        
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
        etiqueta_pc: Label = Label(self.ventana, text="Computadora 1", background="green", foreground="white", font=("Arial", 14))
        etiqueta_pc.place(x=50, y=20)
        etiqueta_jugador_uno: Label = Label(self.ventana, text="Jugador 1", background="green", foreground="white", font=("Arial", 14))
        etiqueta_jugador_uno.place(x=50, y=320)
    
    
    def dibujar_carta(self, x: int = 110, y: int = 143, imagen: str = '/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/juego_21/images/2_de_corazones.png') -> None:
        imagen_canvas: PhotoImage = PhotoImage(file=imagen)
        imagen_canvas = imagen_canvas.subsample(2)
        imagen_label: Label = Label(image=imagen_canvas)
        imagen_label.image = imagen_canvas
        self.canvas.create_image(x, y, image=imagen_canvas)
        
def main() -> None:
    interfaz: InterfazJuegoCartas = InterfazJuegoCartas()
    
if __name__ == '__main__':
    main()