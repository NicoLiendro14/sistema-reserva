# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 278)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_usr = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_usr.setObjectName("label_usr")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_usr)
        self.le_usr = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_usr.setObjectName("le_usr")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_usr)
        self.label_pwd = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_pwd.setObjectName("label_pwd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_pwd)
        self.le_pwd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pwd.setObjectName("le_pwd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_pwd)
        self.label_pwd2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_pwd2.setObjectName("label_pwd2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_pwd2)
        self.le_pwd2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_pwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pwd2.setObjectName("le_pwd2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_pwd2)
        self.label_phone = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_phone.setObjectName("label_phone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_phone)
        self.le_phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_phone.setObjectName("le_phone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_phone)
        self.label_mail = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_mail.setObjectName("label_mail")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_mail)
        self.le_mail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_mail.setObjectName("le_mail")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.le_mail)
        self.btn_acept = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_acept.setObjectName("btn_acept")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.btn_acept)
        self.btn_cancel = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.btn_cancel)
        self.label_warn = QtWidgets.QLabel(self.centralwidget)
        self.label_warn.setGeometry(QtCore.QRect(20, 230, 371, 21))
        self.label_warn.setObjectName("label_warn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crear Usuario"))
        self.label_usr.setText(_translate("MainWindow", "Nombre de usuario:"))
        self.label_pwd.setText(_translate("MainWindow", "Contraseña"))
        self.label_pwd2.setText(_translate("MainWindow", "Repetir contraseña"))
        self.label_phone.setText(_translate("MainWindow", "Telefono:"))
        self.label_mail.setText(_translate("MainWindow", "E-mail"))
        self.btn_acept.setText(_translate("MainWindow", "Aceptar"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancelar"))
        self.label_warn.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">¡Datos incorrectos! Revisar los campos ingresados</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

