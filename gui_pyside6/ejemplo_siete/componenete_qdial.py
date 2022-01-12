from PySide6.QtWidgets import QApplication, QMainWindow, QDial
from PySide6.QtCore import Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        # creamos un nuevo componente QDial es una rueda para aplicaciones de audio por ejemplo
        componente = QDial()
        #componente.setMaximum(10)
        #componente.setMinimum(-10)
        # con setRange se puede establecer el minimo y maximo en una sola linea
        componente.setRange(-8, 8)
        # para mostrar las lineas del dial
        componente.setNotchesVisible(True)
        
        # conectamos el componente a las señales
        componente.valueChanged.connect(self.mostrar_valor)
        componente.sliderMoved.connect(self.mostrar_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)
        
        # se publica el componente
        self.setCentralWidget(componente)

    def mostrar_valor(self, valor):
        print("Valor:", valor)
        
    def mostrar_posicion(self, posicion):
        print(f"Posicion: {posicion}")
        
    def slider_presionado(self):
        print("Slider presionado")
    
    def slider_liberado(self):
        print("Slider liberado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Componentes()
    main.show()
    sys.exit(app.exec_())