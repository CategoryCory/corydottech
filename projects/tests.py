from datetime import date
from django.test import TestCase

from projects.models import Project


class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            name='Test Project',
            summary='Test Summary',
            description='Test Description',
            github_url='https://github.com/TestProject',
            begin_date=date.today(),
        )

    def test_name_max_length(self):
        project = Project.objects.get(pk=1)
        max_length = project._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_slug_max_length(self):
        project = Project.objects.get(pk=1)
        max_length = project._meta.get_field('slug').max_length
        self.assertEqual(max_length, 150)

    def test_summary_max_length(self):
        project = Project.objects.get(pk=1)
        max_length = project._meta.get_field('summary').max_length
        self.assertEqual(max_length, 255)

    def test_status_max_length(self):
        project = Project.objects.get(pk=1)
        max_length = project._meta.get_field('status').max_length
        self.assertEqual(max_length, 25)

    def test_project_slug(self):
        project = Project.objects.get(pk=1)
        self.assertIsNotNone(project.slug)
        self.assertTrue(project.slug.startswith('test-project-'))

    def test_project_status(self):
        project = Project.objects.get(pk=1)
        self.assertEqual(project.status, 'in_progress')

    def test_project_string(self):
        project = Project.objects.get(pk=1)
        self.assertEqual(str(project), 'Test Project')
