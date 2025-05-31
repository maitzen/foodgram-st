from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
        'password',
    )
    search_fields = ('email', 'username')
    search_help_text = 'Поиск по email-адресу и имени пользователя.'
