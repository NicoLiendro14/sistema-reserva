from cancel_ui import *
import bd_conect

class MainWindowCancel(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, pedido , grid,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.bbdd = bd_conect.cls_connect()
        self.pedido1 = pedido
        self.grid1 = grid 
        self.pushButton.clicked.connect(self.cancel_reserva)
        self.pushButton_2.clicked.connect(self.close)

    def cancel_reserva(self):
        #self.buttonBox.eve
        query = "DELETE FROM `labs`.`pedido` WHERE `idpedido`='%s';"%(self.pedido1)
        self.bbdd.run_query(query)
        self.close()