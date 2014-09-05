from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from os import path


class ForgotPasswordEmail():
    """
    Email wrapper class that send forgot email email confirmation URL
    """

    template_text = path.join('mailers', 'reset.txt')
    template_html = path.join('mailers', 'reset.html')

    def __init__(self, to, token, host):
        text_content = render_to_string(self.template_text, {'token': token, 'host': host})
        html_content = render_to_string(self.template_html, {'token': token, 'host': host})
        self.email = EmailMultiAlternatives(
            subject=settings.EMAIL_SUBJECT_PREFIX+"Tautan reset password",
            body=text_content,
            from_email=settings.SERVER_EMAIL,
            to=to
        )
        self.email.attach_alternative(html_content, 'text/html')

    def send(self):
        return self.email.send()
