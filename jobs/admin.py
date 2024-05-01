from django.db import models
from django.contrib import admin
from unfold.admin import ModelAdmin

from jobs.models import Job
from tinymce.widgets import TinyMCE


class JobAdmin(ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', )
    list_filter = ('title', 'company', )
    list_editable = ('start_date', 'end_date', )
    list_display_links = ('title', )
    list_per_page = 20
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }


admin.site.register(Job, JobAdmin)
