from flask_mail import Message
from flask import render_template
from . import mail
from .models import Subscriptions


def send_users_alert(id, **kwargs):
    blog_id = str(id)
    blog_url = '127.0.0.1:5000/blog/'+blog_id+'/'
    subject = 'New Blog Post Alert'
    sender_email = 'esthermutheu99@gmail.com'
    recipients = [subscription.email for subscription in Subscriptions.query.all()]
    email = Message(subject, sender=sender_email, recipients=recipients)
    email.body = render_template("email/send_subscription_alert.txt",blog_url=blog_url, **kwargs)
    email.html = render_template("email/send_subscription_alert.html", blog_url=blog_url, **kwargs)
    mail.send(email)