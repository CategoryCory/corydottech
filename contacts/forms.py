import logging
from datetime import datetime
from django.conf import settings
from django.core import mail
from django.db import transaction
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

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

    def save(self, commit=True, *args, **kwargs):
        instance = super(ContactForm, self).save()

        def send_admin_email():
            message: str = (
                f'You have a new message from {instance.name} ({instance.email}) on cory.tech.\n\n'
                f'{instance.message}'
            )
            try:
                mails_sent: int = mail.send_mail(
                    subject='New message from cory.tech',
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=False,
                )

                if mails_sent < 1:
                    logger.warning(f'Attempt to send mail failed at {datetime.now()}')
            except Exception as e:
                logger.error(
                    f'{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}'
                )

        transaction.on_commit(send_admin_email)
        return instance
