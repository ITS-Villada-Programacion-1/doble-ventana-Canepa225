import sys, os
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMainWindow
from principal import Ui_Buscardor
from resultado import Ui_Resultado

class Resultado(QMainWindow):
    def __init__(self):
        super(Resultado, self).__init__()
        self.ui = Ui_Resultado()
        self.ui.setupUi(self)

    @Slot()
    def cerrar(self):
        self.close()

class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_Buscardor()
        self.ui.setupUi(self)
        self.opened_file = None

    @Slot()
    def buscar(self):
        print("Buscar funciona")
        self.nombre = self.ui.lblNombre.text() #obtengo lo que dice la ventana en el lbl
        self.user = os.popen("whoami").read() #obtengo el user
        self.user = self.user.rsplit() #saco el salto de carro
        self.ruta = "/home/"+self.user[0] #armo la ruta donde voy a ejecutar el comando
        os.chdir(self.ruta) #configura donde se va a ejecutar el comando
        self.resultado = os.popen("find -not -path '*/\.*' | grep '" + self.nombre + "'").read() #guarda en una variable el resultado obtenido del comando
        print(self.resultado)

        self.ventanita = Resultado()
        self.ventanita.ui.txtResultado.setText(self.resultado)
        self.ventanita.show()

    @Slot()
    def borrar(self):
        print("Borrar funciona")
        self.ui.lblNombre.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())