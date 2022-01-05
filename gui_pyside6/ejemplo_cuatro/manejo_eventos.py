# signals (eventos) y slots (metodos que procesan los eventos)

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import QSize
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals y Slots")
        # boton
        boton = QPushButton("Click Aqui")
        # conectamos el evento chequedado, por defecto esta en False
        boton.setCheckable(True)
        # Conectamos otro slot al evento chequear
        boton.clicked.connect(self._evento_chequeado)
        # conectamos el evento signal click con el slot llamado evento_click (funcion)
        boton.clicked.connect(self._evento_click)
        # se publica o muestra el boton
        self.setCentralWidget(boton)
        
    def _evento_click(self):
        # se muestra un mensaje de alerta
        #QMess""ageBox.information(self, "Evento", "Se ha hecho click")
        # accedemosal estado del boton para saber si esta checado o no
        print("evento click: ", self.boton_checado)
        print("evento click")
        
    def _evento_chequeado(self, chequeado):
        # se muestra un mensaje de alerta
        #QMessageBox.information(self, "Evento", "Se ha chequeado")
        self.boton_checado = chequeado
        print("evento chequeado: ", self.boton_checado)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())