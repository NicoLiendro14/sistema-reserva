from user import *
from constantes import *


class pedido():
    def __init__(self, day, start, end, user,lab):
        self.day = day
        self.start = start
        self.end = end
        self.user = user
        self.lab = lab
