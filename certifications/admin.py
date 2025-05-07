from django.contrib import admin
from unfold.admin import ModelAdmin

from certifications.models import Certification


class CertificationAdmin(ModelAdmin):
    list_display = ('name', 'date_earned', )
    list_per_page = 20
    list_display_links = ('name', )


admin.site.register(Certification, CertificationAdmin)
