from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email_shib_user_created(user, http_host):
    tpl_subject = 'emails/shib_user_created_subject.txt'
    tpl_body = 'emails/shib_user_created_body.txt'
    tpl_context = {
        'user': user,
        'http_host': http_host
    }
    subject = render_to_string(tpl_subject, tpl_context).replace('\n', ' ')
    body = render_to_string(tpl_body, tpl_context)
    sender = settings.DEFAULT_FROM_EMAIL
    recipient_list = settings.USER_CREATION_EMAIL_LIST
    send_mail(
        subject,
        body,
        sender,
        recipient_list,
        fail_silently=True
    )
