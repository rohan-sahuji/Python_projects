# Iporting required libraries
from email.message import EmailMessage
import smtplib
import ssl

# App Password for logging in to sender's Email is stored
# in a different file named pass_file in the variable password.
from pass_file import password

# Variables for loging in
email_sender = '' # Input sender's Email address here
email_pass = password

# variables for content of Email
email_receiver = '' # Input receiver's Email address here
subject = 'Email from Python project'
body = '''
Respected Sir,

This is a python generated Email. Do not respond to this. This is just a test mail.

Kind regards,
Python
'''

# Creating instance of EmailMessage
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_receiver, em.as_string())