#!/usr/bin/python
#title			:sendmsg.py.py
#description	:Send Mass Emails
#author			:T. Tyler Daugherty
#date			:20151116
#version		:0.1
#usage			:python sendmsg.py.py
#notes			:
#python_version	:2.7.10
#Copyright 2015 T. Tyler Daugherty. All rights reserved.
#==============================================================================

import csv
import smtplib
from email.mime.text import MIMEText
import re

fp = open('message.txt', 'rb')
msg = MIMEText(fp.read())
fp.close()
msg['Subject'] = 'Mass Mailer Test'
msg['From'] = 'daugherty.tyler.t@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('daugherty.tyler.t@gmail.com', 'Peachtree18!')
email_data = csv.reader(open('email.csv', 'rb'))
email_pattern= re.compile("^.+@.+\..+$")
for row in email_data:
  if( email_pattern.search(row[0]) ):
    del msg['To']
    msg['To'] = row[0]
    try:
      server.sendmail('test@gmail.com', [row[0]], msg.as_string())
    except SMTPException:
      print "An error occured."
server.quit()
