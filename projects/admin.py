from django.db import models
from django.contrib import admin
from unfold.admin import ModelAdmin

from projects.models import Project
from tinymce.widgets import TinyMCE


class ProjectAdmin(ModelAdmin):
    list_display = ('name', 'status', )
    list_filter = ('name', )
    search_fields = ('name', )
    list_display_links = ('name', )
    list_per_page = 20
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }


admin.site.register(Project, ProjectAdmin)
