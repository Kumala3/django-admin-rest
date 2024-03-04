from django.contrib import admin

from .models import TelegramUser, Tire, Height, Width, Diameter

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "first_name", "last_name", "username", "created_at")
    search_fields = ("user_id", "first_name", "last_name", "username")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("created_at", "updated_at")


@admin.register(Tire)
class TireAdmin(admin.ModelAdmin):
    list_display = (
        "brand",
        "diameter",
        "width",
        "height",
        "season",
        "price",
        "discount_percentage",
        "discounted_price",
    )
    list_filter = ("brand", "season", "diameter", "width", "height")
    search_fields = ("brand", "description")


@admin.register(Height)
class HeightAdmin(admin.ModelAdmin):
    list_display = ("value",)
    search_fields = ("value",)


@admin.register(Width)
class WidthAdmin(admin.ModelAdmin):
    list_display = ("value",)
    search_fields = ("value",)


@admin.register(Diameter)
class DiameterAdmin(admin.ModelAdmin):
    list_display = ("value",)
    search_fields = ("value",)
