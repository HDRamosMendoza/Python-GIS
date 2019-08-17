import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "<username>"
gmail_pwd = "<password>"

def mail(to, subject, text, attach):
	msg = MIMEMultipart()

	msg['From'] = gmail_user
	msg['To'] = to
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(attach, 'rb').read())
	Encoders.encode_base64(part)

	part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
	msg.attach(part)

	mailServer =
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, to, msg.as_string())
	mailServer.close()

mail("<email to send to>", "Hola soy tu padre !!", "Este un mensaje de prueba", "catastro_minero.csv")