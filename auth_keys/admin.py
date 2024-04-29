from django.contrib import admin

from auth_keys.models import AuthKey


class AuthKeysAdmin(admin.ModelAdmin):
    list_display = ('id', 'api_key_tag', 'is_active', 'created_at', 'deactivated_at', )
    list_display_links = ('id', )
    list_per_page = 20
    readonly_fields = ('id', 'api_key_tag', 'created_at', 'deactivated_at', )


admin.site.register(AuthKey, AuthKeysAdmin)
