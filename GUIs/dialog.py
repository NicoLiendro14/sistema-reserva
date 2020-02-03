from dialog_ui import *
import sendmail
import bd_conect

class MainWindowDialog(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, data1, pedido1,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.bbdd = bd_conect.cls_connect()
        self.email = None
        self.data = data1
        self.pedido = pedido1
        self.btn_cancel.clicked.connect(self.close)
        self.btn_ok.clicked.connect(self.cancel_reserva)

    def cancel_reserva(self):
        query = "DELETE FROM `labs`.`pedido` WHERE `idpedido`='%s';"%(self.pedido)
        self.bbdd.run_query(query)
        reason = self.le_reason.text()
        subject = "Su reserva ha sido cancelada"
        msj = "Hola "+self.data[0][1]+"! Tu reserva ha sido cancelada. \n Motivo: "+reason+"\n Materia: "+self.data[0][2]+"\n Hora de inicio: "+self.data[0][4]+"\n Hora de fin: "+self.data[0][5]+"\n Dia: "+self.data[0][6]+"\n Laboratorio: "+str(self.data[0][7])
        self.email = sendmail.email_motivo(msj,subject,self.data[0][12])
        self.email.send_mail
        self.close()