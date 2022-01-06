from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import QSize, Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        self.setFixedSize(QSize(400, 300))
        # creamos un componente de tipo etiqueta (label)
        etiqueta = QLabel("Etiqueta")
        # para mostrar el imagen en la etiqueta
        etiqueta.setPixmap(QPixmap("gui_pyside6/ejemplo_siete/20211217_004045.jpg"))
        
        etiqueta.setScaledContents(True)
        
        
        # se publica el componente
        self.setCentralWidget(etiqueta)
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec_()