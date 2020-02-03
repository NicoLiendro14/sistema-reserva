from main_admin import*
from login import *
from user import *
from main_user import *
class controller_login():
    def __init__(self, usr):
        self.grid_admin = None
        self.grid = None
        self.user1 = usr
        self.open_grid()

    def open_grid(self):
        if self.user1.type == 1:
            self.grid = MainWindowUser(self.user1)
            self.grid.show()
        else:
            self.grid_admin = MainWindowAdmin(self.user1)
            self.grid_admin.show()