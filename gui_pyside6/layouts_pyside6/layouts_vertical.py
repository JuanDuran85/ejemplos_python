from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow
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
        # hacemos un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        # se crea un nuevo componente generico para poder publicar el layout
        componente = QWidget()
        componente.setLayout(layout)
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())