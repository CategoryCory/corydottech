from datetime import datetime
from typing import Optional

from ninja import Schema


class TempHumiditySchema(Schema):
    temp_celsius: float
    humidity: float
    read_at: datetime


class TempHumidityResponseSchema(Schema):
    id: Optional[int] = None
    temp_celsius: float
    temp_fahrenheit: float
    humidity: float
    read_at: datetime
