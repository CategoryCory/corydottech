from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.security import APIKeyHeader
from .models import TempHumiditySensor
from .schemas import TempHumiditySchema, TempHumidityResponseSchema
from auth_keys.models import AuthKey


class ApiKey(APIKeyHeader):
    param_name = 'X-API-Key'

    def authenticate(self, request, key):
        api_key = AuthKey.objects.filter(is_active=True).first()
        if key == api_key.api_key:
            return key


router = Router()
header_key = ApiKey()


def temp_humidity_to_response(data: TempHumiditySensor) -> TempHumidityResponseSchema:
    return TempHumidityResponseSchema(temp_celsius=data.temp_celsius,
                                      temp_fahrenheit=data.temp_fahrenheit,
                                      humidity=data.humidity,
                                      read_at=data.read_at)


@router.get('/', response=list[TempHumidityResponseSchema], auth=header_key)
def list_readings(request) -> list[TempHumidityResponseSchema]:
    readings = TempHumiditySensor.objects.all()
    return readings


@router.get('/{reading_id}', response=TempHumidityResponseSchema, auth=header_key)
def get_readings(request, reading_id: int) -> TempHumidityResponseSchema:
    reading = get_object_or_404(TempHumiditySensor, pk=reading_id)
    return temp_humidity_to_response(reading)


@router.post('/', auth=header_key)
def add_reading(request, payload: TempHumiditySchema):
    reading = TempHumiditySensor.objects.create(**payload.dict())
    return {'id': reading.id}
