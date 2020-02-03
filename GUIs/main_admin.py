from dialog import *
from pedido import *
from user import *
from constantes import *
from reserva import *
from main_admin_ui import *
import bd_conect

class MainWindowAdmin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,usr, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.bbdd = bd_conect.cls_connect()
        self.w=None
        self.cancel=None
        self.pushButton_3.clicked.connect(self.cancel_reserva)
        self.user = usr
        self.pedidos = []
        #self.load_grid()
        self.load_grid_lab(1)
        self.load_pedido()
        self.pushButton_4.clicked.connect(self.accept_reserva)
        self.pushButton_5.clicked.connect(self.update_grid)
        #self.pushButton_6.clicked.connect(self.update_grid)
        self.comboBox.currentTextChanged.connect(self.combo)
        self.timer_status = QtCore.QTimer()
        self.timer_status.timeout.connect(self.update_views)
        self.timer_status.start(1000*2)

    def update_views(self):
        self.tableWidget_2.clearContents()
        self.reload_pedido()   

    def update_grid(self):
        #self.combo()
        #self.clean_items_pedido()
        #self.load_pedido()
        #self.tableWidget.clearContents()
        self.tableWidget_2.clearContents()
        self.reload_pedido()
        #self.load_pedido()

    def combo(self):
        print("holi")
        self.clean_items()
        texto = self.comboBox.currentText()
        pos_lab = LABS.get(texto)
        self.load_grid_lab(pos_lab)
    def clean_items(self):
        tam = self.tableWidget.rowCount()
        for i in range(0,self.tableWidget.rowCount(),1):
            for j in range(0,self.tableWidget.columnCount(),1):
                self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(" "))

    def load_grid_lab(self,lab):
        query = "SELECT subject,idstate,hourstart,hourend, day FROM labs.pedido WHERE (lab = '%s' AND idstate=1);"%(lab)
        data = self.bbdd.run_query(query)
        # (('Programacion', 1, '09:00', '12:00', 'Lunes', '1'), ('Python', 1, '10:00', '13:00', 'Miercoles'))
        for y in range(0,len(data),1): #y es cada turno/pedido
            day = self.get_day(data[y][4])
            start = self.get_hours(data[y][2])
            end = self.get_hours(data[y][3])
            for x in range(start,end,1): 
                self.tableWidget.setItem(x,day,QtWidgets.QTableWidgetItem(data[y][0]))
                # self.tableWidget.itemAt(x,day).setBackground(QtGui.QColor(50,255,50)) DAR COLOR A LA CASILLA

    def load_grid(self):
        query = "SELECT subject,idstate,hourstart,hourend, day FROM labs.pedido;"
        data = self.bbdd.run_query(query)
        # (('Programacion', 1, '09:00', '12:00', 'Lunes'), ('Python', 1, '10:00', '13:00', 'Miercoles'))
        for y in range(0,len(data),1): #y es cada turno/pedido
            day = self.get_day(data[y][4])
            start = self.get_hours(data[y][2])
            end = self.get_hours(data[y][3])
            for x in range(start,end,1): 
                self.tableWidget.setItem(x,day,QtWidgets.QTableWidgetItem(data[y][0]))
                # self.tableWidget.itemAt(x,day).setBackground(QtGui.QColor(50,255,50)) DAR COLOR A LA CASILLA

    def get_day(self, day):
        i = DAYS.get(day)
        #pos_day = self.tableWidget.horizontalHeaderItem(i).text() #obtiene el texto del dia
        return i

    def get_hours(self, hours):
        i = HOURS.get(hours)
        #pos_hour = self.tableWidget.verticalHeaderItem(i).text()
        return i


    def reload_pedido(self):
        base = bd_conect.cls_connect()
        query = "SELECT pedido.idstate,pedido.hourstart,pedido.hourend, pedido.day,state.description, pedido.motivo, pedido.user, pedido.idpedido, pedido.lab, pedido.subject FROM labs.pedido INNER JOIN labs.state ON pedido.idstate = state.idstate WHERE pedido.idstate = 2;"
        data = base.run_query(query)
        n = len(data)
        for y in range(0,n,1):
            self.pedidos.append(data[y][7])
            day = data[y][3]
            lab = data[y][8]
            start = data[y][1]
            end = data[y][2]
            state = data[y][4]
            motivo = data[y][5]
            materia = data[y][9]
            self.tableWidget_2.setItem(y,0,QtWidgets.QTableWidgetItem(day))
            self.tableWidget_2.setItem(y,1,QtWidgets.QTableWidgetItem(str(lab)))
            self.tableWidget_2.setItem(y,2,QtWidgets.QTableWidgetItem(materia))
            self.tableWidget_2.setItem(y,3,QtWidgets.QTableWidgetItem(start))
            self.tableWidget_2.setItem(y,4,QtWidgets.QTableWidgetItem(end))
            self.tableWidget_2.setItem(y,5,QtWidgets.QTableWidgetItem(state))
    def load_pedido(self):
        self.clean_items_pedido
        #usr = self.user.usr
        query = "SELECT pedido.idstate,pedido.hourstart,pedido.hourend, pedido.day,state.description, pedido.motivo, pedido.user, pedido.idpedido, pedido.lab, pedido.subject FROM labs.pedido INNER JOIN labs.state ON pedido.idstate = state.idstate WHERE pedido.idstate = 2;"
        data = self.bbdd.run_query(query)
        # ((1, '09:00', '12:00', 'Lunes', 'Reservado'), (1, '10:00', '13:00', 'Miercoles', 'Reservado'))
        # DIA, INICIO, FIN, ESTADO, MOTIVO
        # ((2, '14:00', '17:00', 'Martes', 'Pedido', 'Parcial', 'nicolas14', 6),)
        print(data)
        n = len(data)
        for i in range(0,n-1,1):
            rowpos = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowpos)
        for y in range(0,n,1):
            self.pedidos.append(data[y][7])
            day = data[y][3]
            lab = data[y][8]
            start = data[y][1]
            end = data[y][2]
            state = data[y][4]
            motivo = data[y][5]
            materia = data[y][9]
            self.tableWidget_2.setItem(y,0,QtWidgets.QTableWidgetItem(day))
            self.tableWidget_2.setItem(y,1,QtWidgets.QTableWidgetItem(str(lab)))
            self.tableWidget_2.setItem(y,2,QtWidgets.QTableWidgetItem(materia))
            self.tableWidget_2.setItem(y,3,QtWidgets.QTableWidgetItem(start))
            self.tableWidget_2.setItem(y,4,QtWidgets.QTableWidgetItem(end))
            self.tableWidget_2.setItem(y,5,QtWidgets.QTableWidgetItem(state))

    def cancel_reserva(self):
        row = self.tableWidget_2.currentRow()
        #item = self.tableWidget_2.itemAt(row,0)
        #item1 = item.text()
        #print(item)
        pedido = self.pedidos[row]
        query = "SELECT * FROM labs.pedido INNER JOIN labs.userlab ON pedido.user = userlab.user WHERE idpedido = '%s';"%(pedido)
        data = self.bbdd.run_query(query)
        self.cancel = MainWindowDialog(data,pedido)
        self.cancel.show()

    def accept_reserva(self):
        row = self.tableWidget_2.currentRow()
        pedido = self.pedidos[row]
        query = "UPDATE `labs`.`pedido` SET `idstate`='1' WHERE `idpedido`='%s';"%(pedido)
        self.bbdd.run_query(query)

    def clean_items_pedido(self):
        tam = self.tableWidget_2.rowCount()
        for i in range(0,self.tableWidget_2.rowCount(),1):
            for j in range(0,self.tableWidget_2.columnCount(),1):
                self.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(" "))