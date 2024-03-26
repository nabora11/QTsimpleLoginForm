from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from qTsimpleLoginForm.db import DB



class MainWindow(qtw.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle('Main window')
        self.setFixedSize(350,100)

        self.btn_login=qtw.QPushButton('Login')
        self.btn_register=qtw.QPushButton('Register')
        self.main_layout=qtw.QHBoxLayout()

        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.btn_login)
        self.main_layout.addWidget(self.btn_register)

        self.btn_login.clicked.connect(self.onBtnLogin)

        self.show()
    def onBtnLogin(self):
        self.form=LoginForm()
        self.close()
class LoginForm(qtw.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle('Login window')
        self.setFixedSize(350, 100)
        self.setGeometry(400,400,350,100)
        self.main_layout=qtw.QFormLayout()
        self.setLayout(self.main_layout)
        self.le_user=qtw.QLineEdit()
        self.le_user.setPlaceholderText('user name')
        self.lbl_user=qtw.QLabel('User Name')
        self.le_password=qtw.QLineEdit()
        self.le_password.setPlaceholderText('password')
        self.lbl_password = qtw.QLabel('Password')
        self.btn_submit=qtw.QPushButton('submit')
        self.btn_submit.setFixedSize(100,30)
        self.lbl_user.setObjectName('lbl_username')
        self.lbl_password.setObjectName('lbl_password')
        self.main_layout.addRow(self.lbl_user,self.le_user)
        self.main_layout.addRow(self.lbl_password,self.le_password)
        self.main_layout.addRow(self.btn_submit)
        self.btn_submit.clicked.connect(self.OnBtnSubmit)

        # self.lbl_user.setStyleSheet("color: red;background-color:aqua;")
        self.load=self.read_css('./qTsimpleLoginForm/main_style.css')
        self.setStyleSheet(self.load)
        # self.setStyleSheet('QLabel#lbl_username{color:green;}')
        # self.setStyleSheet('QLabel#lbl_password{color:red;}')


        self.show()


    def read_css(self,name):
        with open(name,"r") as f:
            return f.read()
    def OnBtnSubmit(self):
        user_db=DB()
        self.msg = qtw.QMessageBox()

        if user_db.authenticate(self.le_user.text(),self.le_password.text()):
            # self.msg.setIcon(qtw.QMessageBox.information)
            self.setWindowTitle('Information')
            self.msg.setText('Successfully loged in user')
            self.msg.setStandardButtons(qtw.QMessageBox.Ok)
        else:
            # self.msg.setIcon(qtw.QMessageBox.warning)
            self.msg.show()
            self.setWindowTitle('Warning')
            self.msg.setText('User not found or wrong password')
            self.msg.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        # self.msg.exec()
        self.msg.show()

if __name__ == "__main__":
    app = qtw.QApplication([])
    main_widget = MainWindow()
    app.exec()