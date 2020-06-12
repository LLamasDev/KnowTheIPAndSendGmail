import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email(mensaje):
    email = "your@gmail.com"
    password = "password"
    send_to_email = "send_to@gmail.com"
    subject = "Nueva IP"
    message = mensaje

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = send_to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()