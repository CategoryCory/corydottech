class HomeSensorsRouter:
    model_name = 'temphumidity'
    home_sensors_db = 'home_sensors'

    def db_for_read(self, model, **hints) -> str | None:
        model_name = model._meta.model_name
        if model_name == self.model_name:
            return self.home_sensors_db
        else:
            return None
