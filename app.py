from qTsimpleLoginForm.forms import  *
import sys





if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    main_widget = MainWindow()

    sys.exit(app.exec())