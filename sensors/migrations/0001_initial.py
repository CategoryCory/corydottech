# Generated by Django 5.0.4 on 2024-04-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempHumiditySensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_celsius', models.FloatField(verbose_name='Temperature in Celsius')),
                ('temp_fahrenheit', models.FloatField(verbose_name='Temperature in Fahrenheit')),
                ('humidity', models.FloatField(verbose_name='Relative Humidity in %')),
                ('read_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Temperature/Humidity Reading',
                'verbose_name_plural': 'Temperature/Humidity Readings',
            },
        ),
    ]