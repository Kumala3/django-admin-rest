# Generated by Django 5.0.2 on 2024-03-05 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
        ('rest_api', '0003_diameter_height_width_tire_delete_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "cart_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID товара"
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(default=1, verbose_name="Количество"),
                ),
                (
                    "added_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата добавления"
                    ),
                ),
                (
                    "tire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rest_api.tire",
                        verbose_name="Шина",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rest_api.telegramuser",
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Элемент корзины",
                "verbose_name_plural": "Элементы корзины",
                "db_table": "basket_items",
                "unique_together": {("user", "tire")},
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "order_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID заказа"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                (
                    "is_processed",
                    models.BooleanField(default=False, verbose_name="Обработан"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rest_api.telegramuser",
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Элемент заказа",
                "verbose_name_plural": "Элементы заказа",
                "db_table": "orders_elements",
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(verbose_name="Количество")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="admin_panel.order",
                        verbose_name="Заказ",
                    ),
                ),
                (
                    "tire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rest_api.tire",
                        verbose_name="Шина",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "db_table": "orders",
            },
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
