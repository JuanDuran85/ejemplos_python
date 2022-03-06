"""_summary_

    Enviando correos electronicos con la libreria smtplib

"""

import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

remitente: str = os.getenv("USERNAME")
destinatatio: str = os.getenv("DESTINATIO")
mensaje: str = "Mensaje de prueba desde Python"

username: str = os.getenv("USERNAME")
passwor: str = os.getenv("PASSWORD")

try:
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username, passwor)
    server.sendmail(remitente, destinatatio, mensaje)
    server.quit()    
except Exception as e:
    print(e)

 