from django.db import models


class TempHumidity(models.Model):
    id = models.IntegerField(primary_key=True)
    temp_c = models.FloatField(verbose_name="Temperature in Celsius")
    rel_humidity = models.FloatField(verbose_name="Relative Humidity in %")
    read_at = models.DateTimeField()

    def __str__(self) -> str:
        return f'Temp/Humidity reading at {self.read_at}'

    class Meta:
        managed = False
        db_table = 'temp_humidity'
        verbose_name = 'Temperature and Humidity'
        verbose_name_plural = 'Temperature and Humidity Readings'
