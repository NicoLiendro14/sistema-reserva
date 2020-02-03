from new_user2_ui import *
import bd_conect

class MainWindowNew(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.label_warn.setText(" ")
        self.bbdd = bd_conect.cls_connect()
        self.btn_acept.clicked.connect(self.new_acc)
        self.btn_cancel(self.close)
        #<html><head/><body><p align="center"><span style=" font-weight:600; color:#ff0000;">¡Datos incorrectos! Revisar los campos ingresados</span></p></body></html>
    def new_acc(self):
        usr = self.le_usr.text()
        email = self.le_mail.text()
        query1 = "SELECT user FROM labs.userlab WHERE user = '%s';"%(usr)
        query2 = "SELECT email FROM labs.userlab WHERE email = '%s';"%(email)
        pwd1 = self.le_pwd.text()
        pwd2 = self.le_pwd2.text()
        phone = self.le_phone.text()
        if self.bbdd.run_query(query1):
            print("Ya existe un usuario con esta cuenta!")
            self.label_warn.setText('<html><head/><body><p align="center"><span style=" font-weight:600; color:#ff0000;">Ya existe un usuario con esta cuenta!</span></p></body></html>')
        else:
            if self.bbdd.run_query(query2):
                self.label_warn.setText('<html><head/><body><p align="center"><span style=" font-weight:600; color:#ff0000;">Ya existe un usuario registrado con este e-mail!</span></p></body></html>')
                print("Ya existe un usuario registrado con este e-mail!")
            else:
                if pwd1 != pwd2:
                    print("Las contraseñas no coinciden!")
                    self.label_warn.setText('<html><head/><body><p align="center"><span style=" font-weight:600; color:#ff0000;">Las contraseñas no coinciden!</span></p></body></html>')
                else:
                    query3 = "INSERT INTO `labs`.`userlab` (`password`, `user`, `phone`, `email`, `usertype`) VALUES ('%s', '%s', '%s', '%s', '1');"%(pwd1,usr,phone,email)
                    self.bbdd.run_query(query3)
                    #MOSTRAR VENTANA DE QUE SE CREO CON EXITO EL USUARIO
                    self.close()

