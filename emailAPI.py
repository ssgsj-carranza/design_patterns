# import smtplib
# import ssl
# import getpass
#
# sender_email = "bambigotreaped@yahoo.com"
# receiver_email = "bambigotreaped@yahoo.com"
# message = "Testing"
# smtp_server = "smtp.gmail.com"
# port = 587
# password = getpass.getpass()
#
# context = ssl.create_default_context()
# try:
#     server = smtplib.SMTP(smtp_server, port)
#     server.ehlo()
#     server.starttls(context=context)
#     server.ehlo()
#     server.login(sender_email, password)
# except Exception as e:
#     print("Error, unable to send")
# finally:
#     server.quit()
# server.sendmail(sender_email, receiver_email, message)