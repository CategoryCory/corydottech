from django.contrib import admin

from .models import TempHumidity


class TempHumidityAdmin(admin.ModelAdmin):
    list_display = ('read_at', 'temp_c', 'rel_humidity', )
    list_per_page = 20
    list_display_links = ('read_at', )
    readonly_fields = ('id', 'temp_c', 'rel_humidity', 'read_at', )


admin.site.register(TempHumidity, TempHumidityAdmin)
