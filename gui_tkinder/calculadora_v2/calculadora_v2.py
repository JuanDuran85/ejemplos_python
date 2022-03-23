"""_summary_

    Calculadora con Tkinter

"""

from tkinter import Tk, Label, Entry, Button, Frame, StringVar, IntVar, END, W, E, S, N, messagebox

# Funciones
# funcion reset del boton
def reset() -> None:
    print("reset")

ventana: Tk = Tk()
ventana.title("Calculadora")
ventana.geometry("410x400")
ventana.resizable(0, 0)
ventana.config(bg="gray")

# display de los resultados

pantalla: Entry = Entry(ventana, font=("Arial", 20, "bold"), borderwidth=2, )
pantalla.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

# boton reiniciar la operacion
boton_reset: Button = Button(ventana, text="AC", width=8, height=2, font=("Arial", 10, "bold"), command=lambda: reset())
boton_reset.grid(row=0,column=3, padx=5, pady=10)

ventana.mainloop()