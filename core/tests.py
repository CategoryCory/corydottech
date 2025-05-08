from datetime import date
from io import StringIO
from django.core.management import call_command
from django.test import TestCase

from jobs.models import Job


test_html: str = """<h2>Test Page</h2>
<h3>With a subheading</h3>

<p>This is a test page</p>

<p>It contains:</p>
<ul>
    <li>Formatted data</li>
    <li>Random <strong>bold</strong> text</li>
    <li>Random <em>italic</em> text</li>
</ul>

<p>It also contains:</p>
<ol>
    <li>One item</li>
    <li>Two items</li>
    <li>Three items</li>
</ol>
"""

test_md: str = """## Test Page

### With a subheading

This is a test page

It contains:

  * Formatted data
  * Random **bold** text
  * Random _italic_ text

It also contains:

  1. One item
  2. Two items
  3. Three items
"""


class ConvertHtmlToMdTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Job.objects.create(
            title='Test Job',
            company='Test Company',
            city='Test City',
            state='Test State',
            zipcode='Test Zip Code',
            description=test_html,
            start_date=date(2024, 4, 1)
        )

    def test_convert_html_to_md(self) -> None:
        model_to_test = 'jobs.Job'
        out = StringIO()
        j = Job.objects.get(id=1)
        self.assertEqual(j.description, test_html)
        call_command('convert_html_to_md', model_to_test, stdout=out)
        output = out.getvalue().rstrip('\n')
        output_lines = output.split('\n')
        j = Job.objects.get(id=1)
        self.assertEqual(len(output_lines), 3)
        self.assertEqual(output_lines[0], f"Converting 1 '{model_to_test}' records...")
        self.assertEqual(output_lines[2], f"Finished converting 1 '{model_to_test}' records.")
        self.assertEqual(j.description.strip(), test_md.strip())
