from flask_mail import Message
from app import mail

class EmailService:
    @staticmethod
    def send_email(subject, recipients, body):
        message = Message(subject=subject, recipients=recipients, body=body)
        mail.send(message)
