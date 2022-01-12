from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QStackedLayout, QWidget, QMainWindow
import sys

class Color(QWidget):
    def __init__(self, new_color):
        super().__init__()
        self.setAutoFillBackground(True)
        colors_palette = self.palette()
        colors_palette.setColor(QPalette.Window, QColor(new_color))
        self.setPalette(colors_palette)
        
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts en PySide")
        # Creando un layout QStackedLayout, permite mostrar u layout sobre otro pero uno a la vez cambiando la informacion que se muestra de forma dinamica
        layout_stacked = QStackedLayout()
        # poe defecto solo se visualiza el primer widget agregado
        layout_stacked.addWidget(Color("red"))
        layout_stacked.addWidget(Color("green"))

        # para poder visualizar otro widget se debe llamar a la funcion setCurrentIndex
        layout_stacked.setCurrentIndex(1)
        
        # se crea un nuevo componente generico para poder publicar el layout
        componente = QWidget()
        componente.setLayout(layout_stacked)
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())