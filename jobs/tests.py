from datetime import date
from django.test import TestCase
from .models import Job


class JobModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Job.objects.create(
            title='Test Job',
            company='Test Company',
            city='Test City',
            state='Test State',
            zipcode='Test Zip Code',
            description='Test description',
            start_date=date(2024, 4, 1)
        )

    def test_title_max_length(self):
        j = Job.objects.get(id=1)
        max_length = j._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_company_max_length(self):
        j = Job.objects.get(id=1)
        max_length = j._meta.get_field('company').max_length
        self.assertEqual(max_length, 100)

    def test_city_max_length(self):
        j = Job.objects.get(id=1)
        max_length = j._meta.get_field('city').max_length
        self.assertEqual(max_length, 50)

    def test_state_max_length(self):
        j = Job.objects.get(id=1)
        max_length = j._meta.get_field('state').max_length
        self.assertEqual(max_length, 25)

    def test_zipcode_max_length(self):
        j = Job.objects.get(id=1)
        max_length = j._meta.get_field('zipcode').max_length
        self.assertEqual(max_length, 16)

    def test_is_current(self):
        j = Job.objects.get(id=1)
        self.assertTrue(j.is_current)

    def test_job_string(self):
        j = Job.objects.get(id=1)
        self.assertEqual(str(j), 'Test Job')
