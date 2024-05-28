from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin

from certifications.models import Certification
from tinymce.widgets import TinyMCE


class CertificationAdmin(ModelAdmin):
    list_display = ('name', 'date_earned', )
    list_per_page = 20
    list_display_links = ('name', )
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }


admin.site.register(Certification, CertificationAdmin)
