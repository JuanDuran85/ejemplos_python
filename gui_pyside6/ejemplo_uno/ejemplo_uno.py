import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox

# clase base de Qt (PySide)
# esta clase se encarga de procesar el bucle de eventos (event loop) y solo debe tener un objeto de esta clase
app = QApplication()

# crear un objeto ventana
ventana = QWidget()
# modificando el titulo de la aplicacion
ventana.setWindowTitle("Ejemplo 1")
# modificamos el tamaño de la ventana
ventana.resize(300, 300)
# mostrar la ventana
ventana.show()
sys.exit(app.exec())