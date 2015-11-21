#!/usr/bin/python
#title			:sender2.py
#description	:Sender for mass mail
#author			:T. Tyler Daugherty
#date			:20151120
#version		:0.1
#usage			:python sender2.py
#notes			:
#python_version	:2.7.10
#Copyright 2015 T. Tyler Daugherty. All rights reserved.
#==============================================================================

# erik reed
import smtplib
import csv
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM_ADDRESS = "medlife.uga@gmail.com"
SMTP_SERVER = 'smtp.gmail.com:587'
SMTP_USER = "medlife.uga@gmail.com"
SMTP_PASS = "medlife3"

def mail(msg):
  server = smtplib.SMTP(SMTP_SERVER)
  server.starttls()
  server.login(SMTP_USER,SMTP_PASS)
  server.sendmail(FROM_ADDRESS, msg['To'], msg.as_string())
  server.quit()

f = open('email.csv','rU')
reader = csv.reader(f)
for row in reader:
  text_content = 'Hi ' + str(row[0])
  text_content += \
''',\n\n\tWe wanted to update you as to where you are for the service requirement for Fall 2015 active membership in MEDLIFE at UGA. At this time, we have record of you completing '''
  text_content += str(row[3]) + ' service events towards the required total of 2.'
  text_content += '\n\nIf you think your total is inaccurate, please email medlife.uga@gmail.com with the list of events you have attended and we will be happy to verify!'
  text_content += '\n\nWe still have many opportunities for you to complete this small requirement over the next few weeks, so please be looking for an email from us in the next 24 hours detailing these opportunities!'
  text_content += '\n\nPlease remember the motivation for this standard: service is the essential element in our mission, and participating in these events not only helps those we serve, but is key to a tangible understanding of our mission.'
  text_content += '\n\nDue to this being the introductory semester for this requirement, you will not be marked as inactive yet, but going forward this will be a hard standard.'
  text_content += '\n\nWe are very proud of your involvement with MEDLIFE at UGA, and wish you a wonderful break with tons of MEDLOVE!'
  text_content += '\n\nMEDLIFE at UGA'

  html_content = """\
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <title>Your MEDLIFE Weekly Update, Recap, and Info!</title>
    </head>
    <body style="margin: 0; padding: 0;" link="#C14C43" vlink="#000000">
      <img src="http://www.google-analytics.com/collect?v=1&tid=UA-67269803-1&cid=CLIENT_ID_NUMBER&t=event&ec=email&ea=open&el=recipient_id&cs=newsletter&cm=email&cn=Campaign_Name" />
      <table bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
          <td style="padding: 20px 0 30px 0;">
            <table bgcolor="#ffffff" align="center" style="border: 1px solid #cccccc;" cellpadding="0" cellspacing="0" width="90%">
              <tr><!Header>
                <td bgcolor="#F2F2F2" align="right" style="color: #000000; font-family: Arial, sans-serif; font-size: 9px; padding: 2px 5px 2px 5px">
                  MEDLIFE at UGA Email List. Click here to <a HREF="mailto:listserv@listserv.uga.edu.?subject=signoff medlife&body=signoff medlife"><font color="#000000">Unsubscribe</font></a>
                </td>
              </tr>
              <tr><!Logo Header>
                <td width="90%">
                  <a href="http://medlifeatuga.com/">
                  <img style="display:block;" width="100%" src="https://medlifeatuga.files.wordpress.com/2014/08/cropped-cropped-medlifeprofilepic21.jpg?w=1824" />
                  </a>
                </td>
              </tr>
              <tr>
                  <td align="left" width="65%" style="color: #000000; font-family: Arial, sans-serif; font-size: 20px; padding: 5px 10px 20px 10px">
                  Hey """ + str(row[0]) + """!

                  <p>We wanted to update you as to where you are for the service requirement for Fall 2015 active membership in MEDLIFE at UGA. At this time, <b>we have record of you completing """ + str(row[3]) + """ service events towards the required total of 2.</b></p>

                  <p>If you think your total is inaccurate, please email <a href="mailto:medlife.uga@gmail.com">medlife.uga@gmail.com</a> with the list of events you have attended and we will be happy to verify!</p>

                  <p><b>We still have many opportunities for you to complete this small requirement over the next few weeks, so please be looking for an email from us in the next 24 hours detailing these opportunities!</b></p>

                  <p>Please <b>remember the motivation for this standard:</b> service is the essential element in our mission, and participating in these events not only helps those we serve, but is key to a tangible understanding of our mission.</p>

                  <p>Due to this being the introductory semester for this requirement, you will not be marked as inactive yet, but going forward this will be a hard standard.</p>

                  <p>We are very proud of your involvement with MEDLIFE at UGA, and wish you a wonderful break with tons of MEDLOVE!</p>
                  </td>
                  </tr>
                </td>
                </tr>
                <tr><!Signature>
                      <td align="left" bgcolor="#F2F2F2" style="color: #000000; font-family: Arial, sans-serif; font-size: 14px; padding: 10px 10px 10px 10px">
                        <font color="#C14C43" size="4"> <b>MEDLOVE!</b></font>
                        <br>---
                        <br><b>MEDLIFE at UGA</b><br>
                        <br><b>Co-Presidents:</b> Joe Comer (<a href="mailto:joecomer@uga.edu"><font color="C14C43">joecomer@uga.edu</font></a>) and Alexi Adams (<a href="mailto:alexi@uga.edu"><font color="C14C43">alexi@uga.edu</font></a>)
                        <br><b>Mobile Clinics Chair:</b> Brock Beisel (<a href="mailto:brockbeisel@gmail.com"><font color="C14C43">brockbeisel@gmail.com</font></a>)
                        <br><b>Internal Affairs Chair:</b> Haley Vale (<a href="mailto:hcvale@uga.edu"><font color="C14C43">hcvale@uga.edu</font></a>)
                        <br><b>Social Chair:</b> Dillon Paulo (<a href="mailto:dpaulo@uga.edu"><font color="C14C43">dpaulo@uga.edu</font></a>)
                        <br><b>Service Chair:</b> Justin Choi (<a href="mailto:jbchoi94@uga.edu"><font color="C14C43">jbchoi94@uga.edu</font></a>)
                        <br><b>Public Relations Chair:</b> Tyler Daugherty (<a href="mailto:tydau@uga.edu"><font color="C14C43">tydau@uga.edu</font></a>)
                        <br><b>Treasurer:</b> Sarah Hatton (<a href="mailto:shatton@uga.edu"><font color="C14C43">shatton@uga.edu</font></a>)
                        <br><b>Advertising Chair:</b> Aidan Wells (<a href="mailto:aew48886@uga.edu"><font color="C14C43">aew48886@uga.edu</font></a>)
                        <br><b>Fall Concert Fundraising Chair:</b> Nick Austin (<a href="mailto:njaustin@uga.edu"><font color="C14C43">njaustin@uga.edu</font></a>)
                        <br><b>Sprink 5k Fundraising Chair:</b> Brett Askins (<a href="mailto:askb95@uga.edu"><font color="C14C43">askb95@uga.edu</font></a>)
                        <br><b>Small Fundraising Chairs:</b> Sophie Banspach (<a href="mailto:sophie88@uga.edu"><font color="C14C43">sophieb88@uga.edu</font></a>) and Miranda Martin (<a href="mailto:martinml@uga.edu"><font color="C14C43">martinml@uga.edu</font></a>)
                        <br><br>
                        <font size="2"><center>If you would like to come see us in office hours in the CSO, please consult the <a href="https://www.google.com/calendar/embed?src=jhmj8j2u5kkjq308c7l7qk5nkg%40group.calendar.google.com&ctz=America/New_York"><font color="C14C43">Office Hours Calendar.</font></a> We would love to see you there!</center></font>
                        <br><br>
                        <font size="2"><center><i>Our mission</i> is to help families achieve greater freedom from the constraints of poverty, empowering them to live healthier lives. Our patients did not choose to be poor, but they have chosen to strive toward a better life; MEDLIFE stands beside them in this pursuit. </center></font>
                      </td>
                    </tr>
                </td>
              </tr>
              <tr>
                <td bgcolor="#C14C43" style="color: #000000; font-family: Arial, sans-serif; font-size: 9px; padding: 30px 30px 30px 30px">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr> <!Footer with Copyright and Logos>
                      <td width="75%">
                        &copy; MEDLIFE at UGA 2015<br/>
                        <font color="#000000"><a HREF="mailto:listserv@listserv.uga.edu.?subject=signoff medlife&body=signoff medlife"><font color=#000000>Unsubscribe</font></a> from the MEDLIFE at UGA Listserve</font>
                      </td>
                      <td align="right">
                        <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%">
                          <tr>
                            <td>
                            <a href="https://www.google.com/calendar/embed?src=medlife.uga%40gmail.com&ctz=America/New_York">
                                <img align="middle" src="http://www.iconsdb.com/icons/preview/gray/calendar-xxl.png" alt="Calendar" width="40" hspace="10px" style="display: block;" border="0" />
                            </a>
                          </td>
                          <td>
                            <a href="https://instagram.com/medlifeatuga/">
                            <img align="middle" src="http://www.iconsdb.com/icons/preview/gray/instagram-xxl.png" alt="Instagram" width="40" hspace="5px" style="display: block;" border="0" />
                            </a>
                          </td>
                          <td>
                          <a href="https://www.facebook.com/UGAMedlife">
                            <img align="middle" src="http://www.centerformanifestation.com/images/facebook.png" alt="Facebook" width="40" hspace="5px" style="display: block;" border="0" hspace="20px" />
                          </a>
                          </td>
                          <td>
                          <a href="https://twitter.com/MEDLIFEatUGA">
                                <img align="middle" src="http://ciudadperdida.club/images/twitterB.png" alt="Twitter" width="40" hspace="5px" style="display: block;" border="0" />
                          </a>
                          </td>
                      </tr>
                              </td>
                              </tr>
                              </tr>
                            </table>
                          </td>
                      </td>
                    </tr>
                  </table>
              </td>
              </tr>
            </table>
            </table>
          </td>
        </tr>
    </body>
  </html>
  """

  msg = MIMEMultipart('alternative')
  msg['To'] = str(row[2])
  msg['From'] = FROM_ADDRESS
  msg['Subject'] = """Your current service record for Fall 2015 with MEDLIFE at UGA - """ + str(row[0]) + """ """ + str(row[1])
  msg.add_header('reply-to', FROM_ADDRESS)
  part_text = MIMEText(text_content, 'plain')
  part_html = MIMEText(html_content, 'html')
  msg.attach(part_text)
  msg.attach(part_html)

  mail(msg)
  print('Sent to '+str(row[0])+' '+str(row[1]))
  sleep(1) # pause after each email send
f.close()
