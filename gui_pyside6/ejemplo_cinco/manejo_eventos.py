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
        # conectar a la señal de cambio de titutlo
        self.windowTitleChanged.connect(self._evento_titulo)
        # se publica o muestra el boton
        self.setCentralWidget(self.boton)
        
    def _evento_click(self):
        # cambiar el texto y titulo de la ventana
        self.boton.setText("Nuevo Click")
        self.boton.setEnabled(False)
        self.setWindowTitle("Nuevo Titulo 2")
        print("Evento Click")
        
    def _evento_titulo(self, titulo):
        print(titulo)
        # mostrar el titulo en la barra de estado
        self.statusBar().showMessage(titulo)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())