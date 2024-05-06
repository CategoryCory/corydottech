from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

from .models import Contact


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
            send_mail(
                'New message from cory.tech',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL, ],
                fail_silently=False,
            )

        transaction.on_commit(send_admin_email)
        return instance
