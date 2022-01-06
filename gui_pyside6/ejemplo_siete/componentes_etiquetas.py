from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import QSize, Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        
        # creamos un componente de tipo etiqueta (label)
        etiqueta = QLabel("Etiqueta")
        
        # el metodo settext permite modificar el texto en las etiquetas
        etiqueta.setText("Etiqueta modificada")
        
        # se puede modificar la fuente con el setPointSize
        fuente = etiqueta.font()
        fuente.setPointSize(20)
        etiqueta.setFont(fuente)
        
        # para modificar la alineacion de la etiqueta se puede usar setAligment
        # etiqueta.setAlignment(Qt.AlignCenter)
        
        # otra forma de alinear una etiqueta 
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # se publica el componente
        self.setCentralWidget(etiqueta)
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec_()