from django.db import models


class TempHumiditySensor(models.Model):
    temp_celsius = models.FloatField(verbose_name='Temperature in Celsius')
    temp_fahrenheit = models.FloatField(blank=True, null=True, verbose_name='Temperature in Fahrenheit')
    humidity = models.FloatField(verbose_name='Relative Humidity in %')
    read_at = models.DateTimeField()

    def save(self, *args, **kwargs) -> None:
        if self.temp_fahrenheit is None:
            self.temp_fahrenheit = self.temp_celsius * 1.8 + 32
        super(TempHumiditySensor, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Temp/humidity reading at {self.read_at}'

    class Meta:
        verbose_name = 'Temperature/Humidity Reading'
        verbose_name_plural = 'Temperature/Humidity Readings'
