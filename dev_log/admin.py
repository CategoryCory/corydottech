from django.contrib import admin
from unfold.admin import ModelAdmin

from dev_log.models import DevLogEntry


class DevLogEntryAdmin(ModelAdmin):
    list_display = ('title', 'published_date', 'status', )
    list_filter = ('title', )
    search_fields = ('title', )
    list_display_links = ('title', )
    list_per_page = 20
    readonly_fields = ('slug', )


admin.site.register(DevLogEntry, DevLogEntryAdmin)
