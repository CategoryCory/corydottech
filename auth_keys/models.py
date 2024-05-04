from typing import Any

from cryptography.fernet import Fernet
from django.conf import settings
from django.db import models
from django.utils.safestring import SafeString


class AuthKey(models.Model):
    encrypted_api_key = models.BinaryField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)

    @property
    def api_key(self) -> str:
        cipher = Fernet(settings.ENCRYPTION_KEY)
        return cipher.decrypt(bytes(self.encrypted_api_key)).decode() if self.encrypted_api_key else ''

    def api_key_tag(self) -> Any | SafeString:
        from base64 import b64encode
        return f'{b64encode(self.encrypted_api_key).decode("utf-8")[:10]}...'

    api_key_tag.short_description = 'API Key'
    api_key_tag.allow_tags = True
