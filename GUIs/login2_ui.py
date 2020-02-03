# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 215)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 321, 154))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_usr = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_usr.setObjectName("label_usr")
        self.gridLayout.addWidget(self.label_usr, 2, 1, 1, 1)
        self.label_pwd = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pwd.setObjectName("label_pwd")
        self.gridLayout.addWidget(self.label_pwd, 3, 1, 1, 1)
        self.le_usr = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_usr.setObjectName("le_usr")
        self.gridLayout.addWidget(self.le_usr, 2, 2, 1, 1)
        self.label_error = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_error.setObjectName("label_error")
        self.gridLayout.addWidget(self.label_error, 1, 2, 1, 1)
        self.le_pwd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pwd.setObjectName("le_pwd")
        self.gridLayout.addWidget(self.le_pwd, 3, 2, 1, 1)
        self.label_new = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_new.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_new.setAlignment(QtCore.Qt.AlignCenter)
        self.label_new.setOpenExternalLinks(True)
        self.label_new.setObjectName("label_new")
        self.gridLayout.addWidget(self.label_new, 5, 2, 1, 1)
        self.btn_login = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_login.setObjectName("btn_login")
        self.gridLayout.addWidget(self.btn_login, 4, 2, 1, 1)
        self.btn_new = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_new.setObjectName("btn_new")
        self.gridLayout.addWidget(self.btn_new, 6, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Login", "Login"))
        self.label_usr.setText(_translate("MainWindow", "Usuario:"))
        self.label_pwd.setText(_translate("MainWindow", "Contraseña:"))
        self.label_error.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">Contraseña o usuario incorrecto!</span></p></body></html>"))
        self.label_new.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">¿No tiene cuenta? </span><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">Cree una!</span></p></body></html>"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.btn_new.setText(_translate("MainWindow", "Crear cuenta!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

