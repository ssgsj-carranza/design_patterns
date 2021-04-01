from marketingfirm import MarketingFirm
import smtplib
import ssl

# import getpass

if __name__ == '__main__':
    marketing_firm = MarketingFirm()


sender_email = "sender_email@gmail.com"  # must log in using your email password when prompted
receiver_email = "receiver_email@gmail.com"
message = "Testing"
smtp_server = "smtp.gmail.com"
port = 465
password = input("enter password: ")
server = smtplib.SMTP_SSL(smtp_server, port)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()
