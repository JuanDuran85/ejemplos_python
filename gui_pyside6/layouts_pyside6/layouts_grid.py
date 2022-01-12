from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QGridLayout, QWidget, QMainWindow
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
        # Creando un layout grid
        layout_grid = QGridLayout()
        layout_grid.addWidget(Color('red'), 0, 0)
        layout_grid.addWidget(Color('green'), 0, 1)
        layout_grid.addWidget(Color('blue'), 0, 2)
        layout_grid.addWidget(Color('yellow'), 1, 0)
        layout_grid.addWidget(Color('orange'), 1, 1)
        layout_grid.addWidget(Color('pink'), 1, 2)
        layout_grid.addWidget(Color('purple'), 2, 0)
        layout_grid.addWidget(Color('brown'), 2, 1)
        layout_grid.addWidget(Color('black'), 2, 2)
        
        # se crea un nuevo componente generico para poder publicar el layout
        componente = QWidget()
        componente.setLayout(layout_grid)
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())