from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
import sys

class VentanaPySide():
    def __init__(self):
        self.ventana = QMainWindow()
        self.ventana.setWindowTitle("Ejemplo 2 - POO")
        self.ventana.resize(300, 300)
        

if __name__ == '__main__':
    # el objeto de la clase procesa todos los eventos de la aplicacion, de manea opcional se reciben argumentos con sys.argv desde la linea de comandos
    app = QApplication(sys.argv)
    # creamos un objeto del tipo ventana
    ventana_uno = VentanaPySide()
    ventana_uno.ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())