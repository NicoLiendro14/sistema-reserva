from new_user import *
from controller_login import *
from main_user import *
from login2_ui import *
from user import *

import bd_conect


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.w = None
        self.user = None
        self.control = None
        self.newacc = None 
        self.label_error.setText("")
        self.bbdd = bd_conect.cls_connect()
        self.btn_login.clicked.connect(self.check_login)
        self.btn_new.clicked.connect(self.new_acc)

    def check_login(self):
        usr = self.le_usr.text()
        pwd = self.le_pwd.text()
        query = "SELECT user, password FROM labs.userlab WHERE user ='%s' AND password = '%s';"%(usr,pwd)
        data = "SELECT user, usertype, email FROM labs.userlab WHERE user ='%s';"%(usr)
        if self.bbdd.run_query(query):
            self.user = user(self.bbdd.run_query(data))
            self.control = controller_login(self.user)
            self.close()
        else:
            self.label_error.setText('<html><head/><body><p align="center"><span style=" font-weight:600; color:#ff0000;">Contraseña o usuario incorrecto!</span></p></body></html>')
    def new_acc(self):
        self.new_acc = MainWindowNew()
        self.new_acc.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    myapp = MainWindow()
    myapp.show()
    app.exec()