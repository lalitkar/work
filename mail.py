import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "daddynexwave@gmail.com"
password = '741258963qwerty'


server = smtplib.SMTP(smtp_server,port)
server.ehlo() # Can be omitted
server.starttls() # Secure the connection
server.ehlo() # Can be omitted
server.login(sender_email, password)
server.sendmail('daddynexwave@gmail.com','daddynexwave@gmail.com','hello')
server.close()

