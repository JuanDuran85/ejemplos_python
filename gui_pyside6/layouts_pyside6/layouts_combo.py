from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QMainWindow
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
        # Anidar layouts (layouts dentro de otro layouts)
        # creamos en primer lugarel horizontal y despues el vertical
        layout_horizontal = QHBoxLayout()
        layout_vertical = QVBoxLayout()
        # agregando espacio en el layout vertical
        layout_vertical.setContentsMargins(10, 10, 10, 10)
        layout_vertical.addWidget(Color('red'))
        layout_vertical.addWidget(Color('green'))
        layout_vertical.addWidget(Color('blue'))
        # agregamos el layout vertical dentro del horizontal de manera anidada
        layout_horizontal.addLayout(layout_vertical)
        # se agregan mas elementos al layout horizontal
        layout_horizontal.addWidget(Color('yellow'))
        layout_horizontal.addWidget(Color('orange'))
        
        # se crea un nuevo componente generico para poder publicar el layout
        componente = QWidget()
        componente.setLayout(layout_horizontal)
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())