from PySide2 import *
import main

class Dreamqt(main.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(Dreamqt,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Fantasy Cricket League")

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = Dreamqt()
    qt_app.show()
    app.exec_()

