from email.message import EmailMessage

import ssl
import smtplib






email_sender = 'kvngsley019@gmail.com'
email_password = 'uxshthahpurbiynz'
email_reciever = 'sekixaf374@bodeem.com'
subject ="codewithkingsley is learning new things"
body = """ 'Best python developer'"""
em = EmailMessage()
em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smpt:
    smpt.login(email_sender,email_password)
    smpt.sendmail(email_sender,email_reciever,em.as_string()  )