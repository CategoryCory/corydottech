from cryptography.fernet import Fernet
from datetime import datetime
from django.conf import settings
from django.core.management import BaseCommand
from django.utils.timezone import make_aware
from auth_keys.models import AuthKey


class Command(BaseCommand):
    help = 'Generates a new AuthKey object'

    def add_arguments(self, parser):
        parser.add_argument("new_key", type=str)

    def handle(self, *args, **options):
        # Make sure there is only one active key at a time
        AuthKey.objects.filter(is_active=True).update(deactivated_at=make_aware(datetime.now()))
        AuthKey.objects.filter(is_active=True).update(is_active=False)

        # Create a new AuthKey
        cipher = Fernet(settings.ENCRYPTION_KEY)
        encrypted_key = cipher.encrypt(options['new_key'].encode())
        auth_key = AuthKey(encrypted_api_key=encrypted_key)
        auth_key.save()

        self.stdout.write(self.style.SUCCESS('Successfully saved new AuthKey object.'))
