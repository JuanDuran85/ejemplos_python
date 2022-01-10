from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        # creamos un nuevo componente de checkbox
        checkbox = QCheckBox('Este es un check')
        # activamos el tercer estado
        checkbox.setTristate(True)
        # conectar la señal de cambio de componente|
        checkbox.stateChanged.connect(self.mostrar_status)
        self.setCentralWidget(checkbox)
        
    def mostrar_status(self, estado):
        print(f"Estado inicial: {estado}")
        if estado == Qt.Checked:
            print('Checked: ', estado)
        elif estado == Qt.PartiallyChecked:
            print('PartiallyChecked: ', estado)
        elif estado == Qt.Unchecked:
            print('Unchecked: ', estado)
        else:
            print('Error: ', estado)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Componentes()
    main.show()
    sys.exit(app.exec_())