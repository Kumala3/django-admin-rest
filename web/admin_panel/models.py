from django.db import models

from rest_api.models import Tire, TelegramUser


class CartItem(models.Model):
    """Элемент корзины"""

    cart_id = models.BigAutoField(verbose_name="ID товара", primary_key=True)
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE, verbose_name="Шина")
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.tire} (x{self.quantity}) - {self.user}"

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
        db_table = "basket_items"


class Order(models.Model):
    """Заказ"""

    order_id = models.PositiveIntegerField(verbose_name="ID заказа", primary_key=True)
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_processed = models.BooleanField(default=False, verbose_name="Обработан")

    def __str__(self):
        return f"{self.tire} (x{self.quantity})"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"
        db_table = "orders_elements"


class OrderItem(models.Model):
    """Елемент заказа"""

    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE, verbose_name="Заказ")
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE, verbose_name="Шина")
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return f"Заказ #{self.id} от {self.user}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        db_table = "orders"
