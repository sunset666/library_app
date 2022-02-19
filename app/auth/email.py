from threading import Thread

from flask import render_template, current_app
from flask_mail import Message
from app import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('LibraryApp: Reset Your Password',
               sender=current_app.config['MAIL_SENDER'],
               recipients=[user.email],
               html_body=render_template('email/reset_password.html', user=user, token=token))
