from django.db import models


class TempHumiditySensor(models.Model):
    temp_celsius = models.FloatField(verbose_name='Temperature in Celsius')
    temp_fahrenheit = models.FloatField(verbose_name='Temperature in Fahrenheit')
    humidity = models.FloatField(verbose_name='Relative Humidity in %')
    read_at = models.DateTimeField()

    def __str__(self):
        return f'Temp/humidity reading at {self.read_at}'

    class Meta:
        verbose_name = 'Temperature/Humidity Reading'
        verbose_name_plural = 'Temperature/Humidity Readings'
