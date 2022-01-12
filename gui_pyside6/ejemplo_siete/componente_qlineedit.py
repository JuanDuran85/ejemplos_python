from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import Qt
import sys

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")
        # creamos un nuevo componente QLineEdit
        linea_texto = QLineEdit()
        # establecemos el maximo de carecteras a capturar
        linea_texto.setMaxLength(20)
        # se estable un texto de ayuda
        linea_texto.setPlaceholderText("Escribe aqui")
        # caja de texto en modo solo lectura
        #linea_texto.setReadOnly(True)
        
        # validacion tipo mascara -mask- puede ser numerica o de otro tipo
        linea_texto.setInputMask("aaaaaaaaaaaaaaaaaaaa")
        
        # monitoreando enventos, como enter, cambio de texto, seleccion, entre otros
        # evento enter
        linea_texto.returnPressed.connect(self.enter_persionado)
        # evento seleccion
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        # cambio de texto con textChanged
        linea_texto.textChanged.connect(self.cambio_texto)
            
            
        # se publica el componente
        self.setCentralWidget(linea_texto)

    def enter_persionado(self):
        print("Enter presionado")
        self.centralWidget().setFocus()
        self.centralWidget().setText("nuevo mensaje...")

    def cambio_seleccion(self):
        print("Seleccion cambiada")
        print(self.centralWidget().selectedText())

    def cambio_texto(self):
        print("Cambio de texto")
        print(self.centralWidget().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Componentes()
    main.show()
    sys.exit(app.exec_())