from django.test import TestCase
from django.urls import reverse

from .views import home


class HomeViewTest(TestCase):

    def test_home_page_loads(self) -> None:
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
