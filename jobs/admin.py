from django.contrib import admin
from unfold.admin import ModelAdmin

from jobs.models import Job


class JobAdmin(ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', )
    list_filter = ('title', 'company', )
    list_editable = ('start_date', 'end_date', )
    list_display_links = ('title', )
    list_per_page = 20

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["skills_used"].widget.attrs.setdefault(
            "class",
            (
                "border border-base-200 bg-white min-w-20 placeholder-base-400 rounded-default shadow-xs "
                "text-sm text-mono focus:outline-2 focus:-outline-offset-2 focus:outline-primary-600 "
                "group-[.errors]:border-red-600 focus:group-[.errors]:outline-red-600 dark:bg-base-900 "
                "dark:border-base-700 dark:text-font-default-dark dark:group-[.errors]:border-red-500 "
                "dark:focus:group-[.errors]:outline-red-500 dark:scheme-dark px-3 py-2 w-full max-w-2xl"
            )
        )
        return form


admin.site.register(Job, JobAdmin)
