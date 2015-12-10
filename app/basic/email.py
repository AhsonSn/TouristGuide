from flask_mail import Message
from app import mail

class Email(object):

    @staticmethod
    def send_email(listOfTo, subject, message):
        msg = Message(
            subject,
            sender='orbi0101@gmail.com',
            recipients=listOfTo)

        msg.body = message
        mail.send(msg)
        return True
