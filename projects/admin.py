from django.contrib import admin
from django.forms import BaseModelForm
from unfold.admin import ModelAdmin

from projects.models import Project


class ProjectAdmin(ModelAdmin):
    list_display = ('name', 'status', )
    list_filter = ('name', )
    search_fields = ('name', )
    list_display_links = ('name', )
    list_per_page = 20
    readonly_fields = ('slug', )

    def get_form(self, request, obj=None, **kwargs) -> BaseModelForm:
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["skills_used"].widget.attrs.setdefault(
            "class",
            (
                "border border-base-200 bg-white font-medium min-w-20 placeholder-base-400 rounded-default shadow-xs "
                "text-font-default-light text-sm focus:outline-2 focus:-outline-offset-2 focus:outline-primary-600 "
                "group-[.errors]:border-red-600 focus:group-[.errors]:outline-red-600 dark:bg-base-900 "
                "dark:border-base-700 dark:text-font-default-dark dark:group-[.errors]:border-red-500 "
                "dark:focus:group-[.errors]:outline-red-500 dark:scheme-dark px-3 py-2 w-full max-w-2xl"
            )
        )
        return form


admin.site.register(Project, ProjectAdmin)
