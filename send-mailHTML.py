import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


email_sender = os.environ.get('EMAIL_SENDER')
email_password = os.environ.get('EMAIL_PASSWORD')
email_reciver = os.environ.get('EMAIL_RECIVER')

email_subject = 'Asunto del correo electrónico'


msg = MIMEMultipart('alternative')
msg['Subject'] = email_subject
msg['From'] = email_sender
msg['To'] = email_reciver

html = open("template.html").read().format(Name="HTML")
part2 = MIMEText(html, 'html')
msg.attach(part2)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=email_password)
        connection.sendmail(email_sender, email_reciver, msg.as_string())




