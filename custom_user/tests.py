from django.test import TestCase

from .models import CustomUser


class CustomUserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(
            username='test_user',
            email='test_user@test.com',
            password='123456',
            is_active=True,
            is_staff=False,
            is_superuser=False,
            first_name='Test',
            last_name='User',
        )

    def test_user_full_name(self):
        user = CustomUser.objects.get(pk=1)
        self.assertEqual(user.full_name, 'Test User')

    def test_user_string(self):
        user = CustomUser.objects.get(pk=1)
        self.assertEqual(str(user), 'test_user')
