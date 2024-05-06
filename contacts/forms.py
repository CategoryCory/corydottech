import logging
from datetime import datetime
from django.conf import settings
from django.db import transaction
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from typing import Any

from .models import Contact

logger = logging.getLogger(__name__)


class ContactForm(ModelForm):
    recaptcha = ReCaptchaField(
        required=False,
        widget=ReCaptchaV3(
            attrs={
                'data-theme': 'dark',
                'data-size': 'compact',
            }
        )
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message', 'recaptcha', )
        labels = {'name': 'Name', 'email': 'Email', 'message': 'Message'}

    def save(self, commit=True, *args, **kwargs) -> Any:
        instance = super(ContactForm, self).save()

        def send_admin_email():
            message_body: str = (
                f'<p>You have a new message from {instance.name} ({instance.email}) on cory.tech.</p>'
                f'<p>{instance.message}<p>'
            )
            message = Mail(
                from_email=settings.DEFAULT_FROM_EMAIL,
                to_emails=settings.ADMIN_EMAIL,
                subject='New message from cory.tech',
                html_content=message_body,
            )
            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                logger.info(f'Email sent at {datetime.now()} with status {response.status_code}')
            except Exception as e:
                logger.error(
                    f'{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}'
                )

        transaction.on_commit(send_admin_email)
        return instance
