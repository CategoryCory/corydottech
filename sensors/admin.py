from django.contrib import admin

from .models import TempHumiditySensor


class TempHumiditySensorAdmin(admin.ModelAdmin):
    list_display = ('temp_celsius', 'temp_fahrenheit', 'humidity', 'read_at', )
    list_per_page = 20
    readonly_fields = ('temp_celsius', 'temp_fahrenheit', 'humidity', 'read_at', )


admin.site.register(TempHumiditySensor, TempHumiditySensorAdmin)
