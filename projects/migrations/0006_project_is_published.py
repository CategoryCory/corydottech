# Generated by Django 5.0.4 on 2024-05-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_begin_date_project_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
