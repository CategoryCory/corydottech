from cryptography.fernet import Fernet
from django.conf import settings
from django.test import TestCase

from .models import AuthKey


class AuthKeysTest(TestCase):
    test_encryption_key: str = settings.ENCRYPTION_KEY
    test_api_key: str = "test-api-key"

    @classmethod
    def setUpTestData(cls) -> None:
        cipher = Fernet(cls.test_encryption_key)
        encrypted_key = cipher.encrypt(cls.test_api_key.encode())
        AuthKey.objects.create(encrypted_api_key=encrypted_key)

    def test_decode_api_key(self) -> None:
        key = AuthKey.objects.get(pk=1)
        self.assertEqual(key.api_key, self.test_api_key)
