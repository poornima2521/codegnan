'''
email automation:
-----------------

SMTP (Simple mail transfer protocal):
-----------------------------------
-->This is used to send emails from server to another server.

Note:
-----
1.SMPT SSL port
---------------
465

2.SMPT TLS port
---------------
587

import smtplib

EmailMessage Class
------------------
msg['Subject']='SMTP ON MAIL'
msg['From']='sender@mail.com'
msg['TO']='Receiver@mail.com'

---------------------------
import smtplib
from email.message import EmailMessage
sender = 'poornimapappu18@gmail.com'
password='bdphwpbuwkqrhcmt'
msg = EmailMessage()

msg['Subject'] = 'Welcome Mail'
msg['From'] = sender
msg['To'] = 'sriyaboddeti05@gmail.com'

msg.set_content('Hai sriya')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
'''
------------------------------------
#To send the message to bulk of members in at a time:
'''

import smtplib
from email.message import EmailMessage
sender = 'poornimapappu18@gmail.com'
password='ccwujagwhbgnkydk'
receiver_=['sriyaboddeti05@gmail.com','girishaaa57@gmail.com']
server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login(sender,password)

for email in receiver_:
    msg = EmailMessage()
    msg['Subject']='Welcome Mail'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content('Hai')

    server.send_message(msg)
server.quit


'''









    






