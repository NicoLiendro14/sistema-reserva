# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(393, 222)
        self.label_reason = QtWidgets.QLabel(Dialog)
        self.label_reason.setGeometry(QtCore.QRect(130, 10, 121, 41))
        self.label_reason.setObjectName("label_reason")
        self.le_reason = QtWidgets.QLineEdit(Dialog)
        self.le_reason.setGeometry(QtCore.QRect(60, 50, 271, 111))
        self.le_reason.setCursorPosition(0)
        self.le_reason.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.le_reason.setObjectName("le_reason")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(100, 170, 80, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(220, 170, 80, 23))
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cancelar Reserva"))
        self.label_reason.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Motivo:</span></p></body></html>"))
        self.le_reason.setPlaceholderText(_translate("Dialog", "Ingrese el motivo para cancelar la reserva"))
        self.btn_ok.setText(_translate("Dialog", "Aceptar"))
        self.btn_cancel.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

