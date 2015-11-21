#!/usr/bin/python
#title			:sender_html.py
#description	:HTML/Plain Sender
#author			:T. Tyler Daugherty
#date			:20151120
#version		:0.1
#usage			:python sender_html.py
#notes			:
#python_version	:2.7.10
#Copyright 2015 T. Tyler Daugherty. All rights reserved.
#==============================================================================
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "my@email.com"
you = "your@email.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
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

                </td>
                </tr>
              </td>
              </tr>
              <tr>
                <td bgcolor= "#F2F2F2" align="center" width="35%" style="color: #000000; font-family: Arial, sans-serif; font-size: 18px; padding: 10px 10px 5px 10px">
                  <font size="6"><b>Signup Here</b><br></font>
                  <font size="3"><i>If title is <u>underlined</u>, just click to sign up!</i></font><br><br>

                  <a href="https://www.facebook.com/events/524972264320880/"><font color="C14C43">Mobile Clinics Interest Meeting</font></a><br><font size="3"><i>Thursday, 8 October 2015<br>7:30pm in MLC 148<br></i></font>

                  <p>Bowling with MEDLIFE<br><font size="3"><i>Wednesday, 7 October 2015<br>7:30pm - 9:00pm<br>Showtime Bowling Center<br>555 Macon Hwy<br>Athens, GA 30606<br></i></font></p>

                  <p><a href="http://goo.gl/forms/rtuNNVqxH9"><font color="C14C43">Pruitt Health Bingo</font></a><br><font size="3"><i>Wednesday, 7 October 2015<br>3pm - 4pm<br>960 Hawthorne Ave<br></i></font></p>

                  <p><a href="http://goo.gl/forms/CxmMzwFPQa"><font color="C14C43">Rivers Alive Cleanup</font></a><br><font size="3"><i>Saturday, 10 October 2015<br>9am - 1pm<br>Dudley Park entrance at MLK and E. Broad St.<br></i></font></p>

                  <p>General Body Meeting<br><font size="3"><i>Tuesday, 13 October 2015<br>7:30pm in MLC 102<br></i></font></p>

                  <p><a href="http://goo.gl/forms/pm5kRer3xY"><font color="C14C43">Food 2 Kids</font></a><br><font size="3"><i>Wednesday, 14 October 2015<br>5:30pm to 7:30pm<br>861 Newton Bridge Rd<br>Athens, GA 30607<br></i></font></p>

                  <p><font size="2">If you have signed up for an event and can no longer attend, email <a HREF="mailto:medlife.uga@gmail.com"><font color="#C14C43">medlife.uga@gmail.com</font></a> and include your name and the event you can no longer attend.</p></font>
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
<\html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
