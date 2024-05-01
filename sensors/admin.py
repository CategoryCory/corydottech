from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateTimeFilter

from .models import TempHumiditySensor


class TempHumiditySensorAdmin(ModelAdmin):
    list_display = ('read_at', 'temp_celsius', 'temp_fahrenheit', 'humidity', )
    list_display_links = ('read_at', )
    list_filter = (('read_at', RangeDateTimeFilter), )
    list_per_page = 20
    readonly_fields = ('temp_celsius', 'temp_fahrenheit', 'humidity', 'read_at', )


admin.site.register(TempHumiditySensor, TempHumiditySensorAdmin)
