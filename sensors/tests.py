from datetime import date
from django.test import TestCase

from .models import TempHumiditySensor


class SensorsTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        TempHumiditySensor.objects.create(
            temp_celsius=20.0,
            humidity=50.0,
            read_at=date(2024, 4, 1)
        )

    def test_temp_fahrenheit(self) -> None:
        reading = TempHumiditySensor.objects.get(pk=1)
        expected_temp_f = reading.temp_celsius * 1.8 + 32
        self.assertIsNotNone(reading.temp_fahrenheit)
        self.assertAlmostEqual(reading.temp_fahrenheit, expected_temp_f, delta=0.1)
