from django.contrib import admin

# Register your models here.

from .models import User

@admin.register(User)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("telegram_id", "first_name", "last_name", "username", "created_at")
    search_fields = ("telegram_id", "first_name", "last_name", "username")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
