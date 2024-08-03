from email.message import EmailMessage
from banbo import gmail_key
import ssl
import smtplib


sender = 'oseiowusucurtis@gmail.com'
receiver = 'imfonin@gmail.com'
subject = 'Bring The World Alive'
body = '''Imfonin gives you access to unparalleled selection of photographers. Feast your eyes with outstanding images'''

email = EmailMessage()
email['From'] = sender
email['To'] = receiver
email['Subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
	smtp.login(sender, gmail_key)
	smtp.sendmail(sender, receiver, email.as_string())

print('Email sent successfully Mr. Awuku')
