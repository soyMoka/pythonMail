import os
import ssl
import smtplib
from email.message import EmailMessage


email_sender = os.environ.get('EMAIL_SENDER')
email_password = os.environ.get('EMAIL_PASSWORD')
email_reciver = os.environ.get('EMAIL_RECIVER')


# Aquí va el aunto del correo a mandar
email_subject = 'prueba del cosito'

#Este es el cuerpo de texto del correo... vamos, el correo en si.
email_body = """
vamos a probar si imprime el mensaje al final de la ejecucion

ahora me despido, SMK.
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_reciver
em['Subject'] = email_subject
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciver, em.as_string())
    print("creo que ya está")

