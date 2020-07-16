#!/bin/bash/python3
import smtplib
from email.mine.multipart import MIMEMultipart
from email.mine.text import MIMEText
mail_content = '''
Testing .
'''

#the mail address and password
server_address = 'mamabapuni@gmail.com'
sender_pass = 'darknightrotler@gmail.com'
reciever_address = 'mamabapuni@gmail.com'
#setup the MIME
message =  MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_Address
message[ 'Subject' ] = 'Testing status'
#body and attachment
message.attach(MIMEText(mail_content,'plain'))
#smtp session to send the mail
session = smtp.SMTP('smtp.gmail.com',587) #use gmail with port
session.starttls() #enable security
session.login(sender_address,sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address,reciever_address,text)
session.quit()
print('Mail has been sent')
