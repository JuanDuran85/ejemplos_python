from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtCore import Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        # creamos un nuevo componente QSlider que por defecto viene en vertical
        componente = QSlider(Qt.Horizontal)
        #componente.setMaximum(10)
        #componente.setMinimum(-10)
        # con setRange se puede establecer el minimo y maximo en una sola linea
        componente.setRange(-10, 10)
        
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