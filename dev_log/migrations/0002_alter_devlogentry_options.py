# Generated by Django 5.2.4 on 2025-07-13 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dev_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devlogentry',
            options={'ordering': ('-published_date',), 'verbose_name': 'Dev Log Entry', 'verbose_name_plural': 'Dev Log Entries'},
        ),
    ]
