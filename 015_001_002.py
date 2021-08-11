
import smtplib
from email.message import EmailMessage

smtp = smtplib.SMTP_SSL('smtp.zone.eu', 465)
smtp.login('python@mrartful.com', 'AcD4345ikl12')

msg = EmailMessage()
msg['Subject'] = 'Test email written by python'
msg['From'] = 'python@mrartful.com'
msg['To'] = 'tratevs@gmail.com'
msg.set_content('This is a sample email that was created and sent by python script')
msg.add_alternative("""
<h1> Hello world</h1>
<p style = "color : red">
This is a sample email that was created and sent by python script
</p>
""", subtype='html')

smtp.send_message(msg)