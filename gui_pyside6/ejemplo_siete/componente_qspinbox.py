from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox
from PySide6.QtCore import Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        # creamos un nuevo componente QSpinBox para seleccionar un valor numerico demanera individual, no trabaja con valores flotantes
        numero = QSpinBox()
        # QDoubleSpinBox() es paa valores flotantes
        
        # establecemos el rango de valores por separado o por un solo rango
        numero.setMaximum(-10)
        numero.setMaximum(10)
        # se puede usar diractamente el metodo setRange()
        #numero.setRange(-10, 10)
        
        # se puede establecer prefijos o sufijos al termino
        numero.setPrefix("$")
        numero.setSuffix("€")
        
        # indicando los incrementos cada vez que se utilizan las flechas oara icrementar o decrementar, no sobrepasa los limites indicados
        numero.setSingleStep(3)
        
        # se publica el componente
        self.setCentralWidget(numero)
        
        # conectando a las señales que se pueden trabajar con el componente
        # evento o señal de cambio de valor, enviando el valor nuevo pero solo el numerico
        numero.valueChanged.connect(self.mostrar_valor)
        # texto incluyendo prefijo y sufijo
        numero.textChanged.connect(self.mostrar_texto)
        
    def mostrar_valor(self, valor):
        print(valor)
        
    def mostrar_texto(self, texto):
        print(texto)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Componentes()
    main.show()
    sys.exit(app.exec_())