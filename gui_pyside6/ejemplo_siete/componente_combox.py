from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        # creamos un nuevo combo box (drop down list)
        combo_box = QComboBox()
        # agregamos elementos
        combo_box.addItem('Item 1')
        combo_box.addItems(['Item 2', 'Item 3', 'Item 4'])
        
        # se monitorea el cambio del elemento seleccionado por indice
        combo_box.currentIndexChanged.connect(self.mostrar_indice)
        # monitorear el cambio en el estado pero en el texto
        combo_box.currentTextChanged.connect(self.mostrar_texto) 
           
        # se publica el componente
        self.setCentralWidget(combo_box)
        
        
    def mostrar_indice(self, indice):
        print(f"Indice: {indice}")
        
    def mostrar_texto(self, texto):
        print(f"Texto: {texto}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Componentes()
    main.show()
    sys.exit(app.exec_())