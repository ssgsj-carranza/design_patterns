import smtplib
import ssl
from contestants import Contestant

sender_email = "example@gmail.com"
receiver_email = "yourexample@gmail.com"
message = Contestant()
smtp_server = "smtp.gmail.com"
port = 587
password = input("Type password and press enter: ")

context = ssl.create_default_context()
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
except Exception as e:
    print("Error, unable to send")
finally:
    server.quit()
server.sendmail(sender_email, receiver_email, message)