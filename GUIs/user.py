class user():
    def __init__(self,data):
        self.usr=data[0][0]
        self.type=data[0][1]
        self.email=data[0][2]

    def get_usr(self):
        return self.usr

    def get_type(self):
        return self.type

    def get_email(self):
        return self.email