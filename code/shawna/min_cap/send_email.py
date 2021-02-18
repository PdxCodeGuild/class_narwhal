import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()

# Passwords, Logins, Recipient Emails / Phone Numbers

PASSWORD = os.getenv('GOOGLE_PASSCODE') #password is stored in a .env file and since account has 2 factor auth the password is a google generated pass that includes the auth.
MY_EMAIL = os.getenv('EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')

#Construct Message
def send_email():
    msg = EmailMessage()
    msg['Subject'] = 'My Test Subject'
    msg['From'] = 'This does not seem to matter'
    msg['TO'] = TO_EMAIL
    msg.set_content('This is a test message')

    #Log into mail server

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: #(gmail mail server, port number)

        smtp.login(MY_EMAIL, PASSWORD)
        
        #Send Message
        
        smtp.send_message(msg)
        







