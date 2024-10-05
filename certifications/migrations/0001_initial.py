# Generated by Django 5.0.6 on 2024-05-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('source', models.TextField(blank=True, max_length=100, null=True)),
                ('date_earned', models.DateField()),
            ],
        ),
    ]