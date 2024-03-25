from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys



class MainWindow(qtw.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle('')
        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    main_widget = MainWindow()

    sys.exit(app.exec())

