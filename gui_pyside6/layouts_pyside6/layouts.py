from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6.QtCore import Qt
import sys

class Color(QWidget):
    def __init__(self, new_color):
        super().__init__()
        # indicamos que se puede agregar un nuevo color de fondo al componente
        self.setAutoFillBackground(True)
        colors_palet = self.palette()
        # creamos el componente de color de fondo aplicando el nuevo color
        colors_palet.setColor(QPalette.Window, QColor(new_color))
        # aplicamos el nuevo color al componente
        self.setPalette(colors_palet)
        
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts en PySide")
        component_with_color = Color('green')
        # el componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(component_with_color)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())
    