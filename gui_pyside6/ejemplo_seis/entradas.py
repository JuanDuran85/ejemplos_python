# signals (eventos) y slots (metodos que procesan los eventos)

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import QSize
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals y Slots")
        self.setFixedSize(400,200)
        # se define la etiqueta y la linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # conectar el wiget de entrada_texto con la etiqueta
        # la señal es textChanged y el slot es setText(etiqueta o label)
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # layout agregar varios elementos a nuestra ventana
        # publicamos los componentes usando un layout
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        # crear un contenedor para publicar el layout
        contenedor = QWidget()
        contenedor.setLayout(disposicion)
        # se publica el contenedor, el cual incluye los demas elementos
        self.setCentralWidget(contenedor)
                       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())