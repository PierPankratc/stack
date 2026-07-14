import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"



class Email:

    def __init__(self, 
                 login = 'login@gmail.com', 
                 password = 'qwerty',
                 subject = 'Subject',
                 recipients = ['vasya@email.com', 'petya@email.com'],
                 message = 'Message',
                 header = None):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header


    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        send_msg = smtplib.SMTP(GMAIL_SMTP, 587)
        send_msg.ehlo()
        send_msg.starttls()
        send_msg.login(user=self.login, password=self.password)
        send_msg.sendmail(from_addr=self.login, to_addrs=self.recipients, msg=msg.as_string())
        send_msg.ehlo()


    def recieve(self):
        recieve_mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        recieve_mail.login(user=self.login, password=self.password)
        recieve_mail.list()
        recieve_mail.select(mailbox='INBOX')
        criterion = f'(HEADER Subject "{self.header}")' if self.header else 'ALL'
        result, data = recieve_mail.uid('search', None, criterion)
        if data:
            latest_email_uid = data[0].split()[-1]
            result, data = recieve_mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1] if data[0][1] else None
            if raw_email:
                email_message = email.message_from_bytes(raw_email)
            recieve_mail.logout()
            return {
                'uid': latest_email_uid,
                'data': email_message 
            }
        
if __name__ ==  '__main__':
    email_messager = Email()
    email_messager.send_message()
    received = email_messager.recieve()









