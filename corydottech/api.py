from ninja import NinjaAPI
from sensors.api import router as sensors_router

api = NinjaAPI()


api.add_router('sensors/', sensors_router)
