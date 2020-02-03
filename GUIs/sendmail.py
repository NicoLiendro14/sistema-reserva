from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class email_motivo:
    def __init__(self,message,subject,email):
        # crear instancia de objeto de mensaje
        self.msg = MIMEMultipart()
        self.message = message #Mensaje que recibe el usuario con motivo de rechazo/horario de reserva
        # seteando los parametros del msj
        password = "nicocentra7"
        self.msg['From'] = "nicolasliendro0697@gmail.com"
        self.msg['To'] = email
        self.msg['Subject'] = subject
        # añadir el mensaje en el cuerpo
        self.msg.attach(MIMEText(message, 'plain'))
        #creando el servidor
        self.server = smtplib.SMTP('smtp.gmail.com: 587')
        self.server.starttls()
        # Logeandose para mandar el mail
        self.server.login(self.msg['From'], password)
        self.send_mail()
    def send_mail(self):
        # enviando el msj por el servidor
        self.server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        self.server.quit()
        print ("Email enviado correctamente a %s:" % (self.msg['To']))

#if __name__ == "__main__":
#    app = email_motivo("Hola bobo","ASUNTO XD","nick.sfra.7@gmail.com")
#    app.send_mail()