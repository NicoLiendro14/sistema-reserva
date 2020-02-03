from bd_conect import *
from pedido import *
from reserva2_ui import *


class MainWindowReserva(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, pedido,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.pedido = pedido
        self.bbdd = cls_connect()
        self.setupUi(self)
        self.load_pedido()
        self.pushButton_2.clicked.connect(self.create_pedido)
        self.pushButton.clicked.connect(self.close)

    def load_pedido(self):
        self.lineEdit.setText(self.pedido.day)
        self.lineEdit_2.setText(self.pedido.start)
        self.lineEdit_3.setText(self.pedido.end)
        self.lineEdit_6.setText(str(self.pedido.lab))
        

    def create_pedido(self):
        #materia = self.lineEdit_5.text()
        query = "INSERT INTO `labs`.`pedido` (`user`, `subject`, `idstate`, `hourstart`, `hourend`, `day`, `lab`, `motivo`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(self.pedido.user,self.lineEdit_5.text(),2,self.pedido.start,self.pedido.end,self.pedido.day,self.pedido.lab,self.lineEdit_4.text())
        self.bbdd.run_query(query)
        self.close()
        #usr = self.pedido.user.usr
        #sub = "AyED"
        #id = 2
        #start = self.pedido.start
        #end = self.pedido.end
        #day1 = self.pedido.day

        #motivo = self.lineEdit_4.text()

        #query = "INSERT INTO `labs`.`pedido` (`user`, `subject`, `idstate`, `hourstart`, `hourend`, `day`, `lab`, `motivo`) 
        #VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%()
        # query = "INSERT INTO iris (sepalLength, sepalWidth, petalLength, petalWidth, idType) VALUES ('%s','%s','%s','%s','%d');"%(sepalL, sepalW, petalL, petalW, idT)
        # 
