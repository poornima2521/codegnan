'''
Date and time:
-------------
-->Python provide the built in datetime module to work with date and time..

import datetime
-------------

import datetime
today =  datetime.date.today()
now=datetime.datetime.now()
print(now)
print(today)

import datetime
now=datetime.datetime.now()
print(f"Year is : {now.year}")
print(f"Month is : {now.month}")
print(f"Day is : {now.day}")
print(f"Hour is: {now.hour}")
print(f"Minutes is : {now.minute}")
print(f"Second is : {now.second}")


Formatting date and time
-----------------------
-->strftime() is used to formate date and time

%d --> daY
%m -->month
%y -->year
%H -->hour
%M -->minute
%s -->second

import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))

import datetime
date_1 =datetime.date(2026,6,1)
date_2 =datetime.date(2026,6,15)
differ=date_1-date_2
print(differ)

import datetime
date_1 =datetime.date(2025,6,1)
date_2 =datetime.date(2026,6,15)
differ=date_2-date_1
print(differ)

timedelta
---------

import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days = 7)  #  2026-06-22
print(future)


import datetime
day = datetime.date.today()   # 0
print(day.weekday())

import datetime
day = datetime.date.today()   # Mon Jun 15 00:00:00 2026
print(day.ctime())

import calendar
import datetime
today= datetime.date.today()
year=today.year
month= today.month
print(calendar.month(year,month))

Output:
     June 2026
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30

import calendar
year=2025
month=7
print(calendar.month(year,month))

import calendar
year=2025
print(calendar.calendar(2025))

#To find leap year or not
import calendar
year=2024
print(calendar.isleap(year))

#To write the program to send the message in a particular time mention to particular mail
'''
import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

sender_mail = "poornima.pappu05@gmail.com"
password = "qsns tmnz xsth edou"
receiver_mail = "venkateshgirisha14@gmail.com"
send_time = "2026-06-15 10::00"

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if now >= send_time:
        msg = EmailMessage()
        msg["Subject"] = "Test Mail"
        msg["From"] = sender_mail
        msg["To"] = receiver_mail
        msg.set_content("Hello, this mail was sent automatically at the scheduled time.")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_mail, password)
            smtp.send_message(msg)

        print("Mail Sent Successfully!")
        break

    time.sleep(1)



    




























