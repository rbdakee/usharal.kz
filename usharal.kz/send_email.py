from email.message import EmailMessage
import ssl
import smtplib

def send_link(body, email_receiver):
    email_sender = 'usharal.market@gmail.com'
    email_password = 'vlhjijyuxalcarhm'
    subject = 'СБРОСИТЬ ПАРОЛЬ'
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print('Письмо отправлено')

