"""_summary_

    Juego Siete Afortunado en Tkinter con clases

"""

import random
from tkinter import BOTTOM, Button, Label, PhotoImage, StringVar, Tk, mainloop
from typing import Literal

class SieteAfortunado:
    def __init__(self) -> None:
        self.crear_interfaz()
        
    def crear_interfaz(self)-> None:
        ventana: Tk = Tk()
        ventana.minsize(width=340, height=450)
        ventana.geometry("340x450")
        
        boton: Button = Button(ventana, text="Jugar", command=self.jugar, font='arial 18 bold')
        boton.pack()
        
        foto: PhotoImage = PhotoImage(file="/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/juego_siete_afortunado/img/dinero.png")
        self.gano = Label(ventana, image=foto)
        
        self.campos: list = [StringVar() for _ in range(3)]
        posicion: int = 10
        for campo in self.campos:
            label: Label = Label(ventana, textvariable=campo, background='White', foreground='Black' ,font='arial 42 bold')
            label.place(x=posicion, y=100, width=100, height=100)
            posicion += 110
               
        mainloop()
        
    def generar_numero(self) -> int:
        return random.randint(0, 9)
        
    def jugar(self) -> None:
        hay_siete: Literal = False
        for i in range(3):
            valor: int = self.generar_numero()
            self.campos[i].set(valor)
            if valor == 7:
                hay_siete = True
        if hay_siete:
            self.gano.pack(side=BOTTOM)
        else:
            self.gano.pack_forget()
        
if __name__ == "__main__":
    jugar: SieteAfortunado = SieteAfortunado()