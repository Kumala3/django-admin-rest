from django.contrib import admin

from .models import CartItem, OrderItem, Order

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("user", "tire", "quantity", "added_at")
    list_filter = ("user", "added_at")
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "tire__brand",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "is_processed")
    list_filter = ("is_processed", "created_at")
    search_fields = ("user__username", "user__first_name", "user__last_name")
    date_hierarchy = "created_at"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'tire', 'quantity')
    list_filter = ('order', 'tire')
    search_fields = ('order__id', 'tire__brand')
