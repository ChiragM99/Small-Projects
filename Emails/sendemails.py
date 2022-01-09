import smtplib 
from email.message import EmailMessage 
from string import Template 
from pathlib import Path 

email = EmailMessage()
email['from'] = 'Username'
email['to'] = 'myemail@gmail.com'
email['subject'] = 'python email test'

email.set_content('Content can be text,html,image..')

#use smtp server to login to gmail client and send email from there
with smtplib.SMTP(hose = 'smtp.gmail.com', port = 587) as smtp: 
    smtp.ehlo() 
    smtp.starttls() #encryption mechanism to connect securley to the server
    smtp.login('myemail@gmail.com', 'password')
    smtp.send_message(email)
    print('Finished')

# We want to customize the email to each specific person -multiple users
html = Template(Path('index.html').read_text()) 
email.set_content(html.substitute({'name' : 'Tom'}), 'html')