import smtplib
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('data.cfg')


def send_mail(to_address, subject, message_content):
    from_address = config.get('MailingCredentials', 'fromMail')
    password = config.get('MailingCredentials', 'fromPassword')
    msg = 'To: %s\r\nSubject: %s\r\n\r\n%s' % (to_address, subject, message_content)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg)
    server.quit()