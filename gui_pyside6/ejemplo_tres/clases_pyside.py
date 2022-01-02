from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import QSize
import sys

class VentanaPySide(QMainWindow):
    def __init__(self):
        # llamamos al metodo init de la clase padre
        super().__init__()
        self.setWindowTitle("Ejemplo 2 - POO")
        # para agregar valor de inicio que se puede modificar
        # self.resize(300, 300)
        # para agregar valores fijos a la ventana
        self.setFixedSize(QSize(400, 300))
        # creamos algubos componentes
        self._agregar_componentes()
        
    def _agregar_componentes(self):
        # agregando un menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # agregamos algunas opciones al menu
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo .addAction(accion_nuevo)
        # agregnaod texto en la parte inferior de la barra de estado
        accion_nuevo.setStatusTip('Crear un nuevo archivo')
        # agregamos un mensaje en la barra de estado
        self.statusBar().showMessage('Bienvenido a PySide')
        # agregamos un componente de boton
        boton = QPushButton('Aceptar', self)
        # agregando en la parte central de la ventana el boton
        self.setCentralWidget(boton)
        

if __name__ == '__main__':
    # el objeto de la clase procesa todos los eventos de la aplicacion, de manea opcional se reciben argumentos con sys.argv desde la linea de comandos
    app = QApplication(sys.argv)
    # creamos un objeto del tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())