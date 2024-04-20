from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'full_name', )
    search_fields = ('username', 'email', 'full_name')
    list_per_page = 20


admin.site.register(CustomUser, CustomUserAdmin)
