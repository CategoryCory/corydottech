from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'received_at', )
    list_display_links = ('name', )
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
