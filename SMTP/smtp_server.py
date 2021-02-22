import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email.utils import formatdate
import datetime
import os

COMMASPACE = ', '

smtpUser = 'amazon42342@gmail.com'
smtpPass = '581688jl'

toAdd = ''
fromAdd = smtpUser

today = datetime.date.today()

subject = 'Data File 01 %s' % today.strftime('%Y %b %d')
header = 'To :' + toAdd + '\n' + 'From : ' + fromAdd + '\n' + 'Subject : ' + subject + '\n'
body = 'This is a data file on %s' % today.strftime('%Y %b %d')

attach = 'Data on %s.jpg' % today.strftime('%Y-%m-%d')

def sendMail(to, subject, text, files=[]):
    assert type(to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = smtpUser
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file,"rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        # Attach the attachment to the MIMEMultipart object
        msg.attach(part)

    #server = smtplib.SMTP('smtp.mail.ru:587')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(smtpUser,smtpPass)
    server.sendmail(smtpUser, to, msg.as_string())

    server.quit()