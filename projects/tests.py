from datetime import date
from django.test import TestCase

from projects.models import Project


class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            name='Test Project 1',
            summary='Test Summary 1',
            description='Test Description 1',
            github_url='https://github.com/TestProject',
            begin_date=date.fromisoformat('2024-02-01'),
        )
        Project.objects.create(
            name='Test Project 2',
            summary='Test Summary 2',
            description='Test Description 2',
            github_url='https://github.com/TestProject',
            status=Project.COMPLETE,
            begin_date=date.fromisoformat('2024-02-01'),
            end_date=date.fromisoformat('2024-04-01'),
        )
        Project.objects.create(
            name='Test Project 3',
            summary='Test Summary 3',
            description='Test Description 3',
            github_url='https://github.com/TestProject',
            status=Project.COMPLETE,
            begin_date=date.fromisoformat('2024-02-01'),
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
        self.assertEqual(str(project), 'Test Project 1')

    def test_date_str_in_progress(self):
        project = Project.objects.get(pk=1)
        expected_date_str = f'{project.begin_date.strftime("%b %Y")} \u2013 PRESENT'
        self.assertEqual(project.date_str, expected_date_str)

    def test_date_str_complete_with_end_date(self):
        project = Project.objects.get(pk=2)
        expected_date_str = f'{project.begin_date.strftime("%b %Y")} \u2013 {project.end_date.strftime("%b %Y")}'
        self.assertEqual(project.date_str, expected_date_str)

    def test_date_str_complete_without_end_date(self):
        project = Project.objects.get(pk=3)
        expected_date_str = project.begin_date.strftime("%b %Y")
        self.assertEqual(project.date_str, expected_date_str)
