# signals (eventos) y slots (metodos que procesan los eventos)

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import QSize
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals y Slots")
        # boton
        self.boton = QPushButton("Click Aqui")
        # conectamos el evento chequedado, por defecto esta en False
        # asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self._evento_click)
        # se publica o muestra el boton
        self.setCentralWidget(self.boton)
        
    def _evento_click(self):
        # cambiar el texto y titulo de la ventana
        self.boton.setText("Nuevo Click")
        self.boton.setEnabled(False)
        self.boton.setWindowTitle("Nuevo Titulo")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())