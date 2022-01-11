from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        # creamos un nuevo componente QlistWidget
        lista = QListWidget() 
        lista.addItems(['Item 1', 'Item 2', 'Item 3', 'Item 4'])
        # monitorear ek canbio del elemento seleccionado, tanto el elemento con el texto
        lista.currentItemChanged.connect(self.mostrar_indice)
        lista.currentTextChanged.connect(self.mostrar_texto)
        
        # se publica el componente
        self.setCentralWidget(lista)

    def mostrar_indice(self, item):
        print(f"Indice: {item.text()}")
        
    def mostrar_texto(self, texto):
        print(f"Texto: {texto}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Componentes()
    main.show()
    sys.exit(app.exec_())