from django.db import models


class TelegramUser(models.Model):
    user_id = models.IntegerField(verbose_name="ID пользователя", unique=True)
    first_name = models.CharField(verbose_name="Имя пользователя", max_length=255)
    username = models.CharField(
        verbose_name="Username пользователя", max_length=255, null=True, blank=True
    )
    last_name = models.CharField(
        verbose_name="Фамилия пользователя", max_length=255, null=True, blank=True
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    is_admin = models.BooleanField(verbose_name="Администратор", default=False)
    phone_number = models.CharField(
        max_length=20, verbose_name="Номер телефона", blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username}-{self.user_id}"

    class Meta:
        db_table = "users"


class Diameter(models.Model):
    value = models.IntegerField(unique=True, verbose_name="Диаметр")

    def __str__(self):
        return f'{self.value}"'

    class Meta:
        verbose_name = "Диаметр"
        verbose_name_plural = "Диаметры"
        db_table = "diameters"


class Width(models.Model):
    value = models.IntegerField(unique=True, verbose_name="Ширина")

    def __str__(self):
        return f"{self.value} мм"

    class Meta:
        verbose_name = "Ширина"
        verbose_name_plural = "Ширины"


class Height(models.Model):
    value = models.IntegerField(unique=True, verbose_name="Высота")

    def __str__(self):
        return f"{self.value} мм"

    class Meta:
        verbose_name = "Высота"
        verbose_name_plural = "Высоты"
        db_table = "heights"


class Tire(models.Model):
    SEASONS = [("W", "Зима"), ("S", "Лето"), ("A", "Всесезонные")]

    brand = models.CharField(max_length=100, verbose_name="Бренд, модель")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    diameter = models.ForeignKey(
        Diameter, on_delete=models.CASCADE, verbose_name="Диаметр"
    )
    width = models.ForeignKey(Width, on_delete=models.CASCADE, verbose_name="Ширина")
    height = models.ForeignKey(Height, on_delete=models.CASCADE, verbose_name="Высота")
    season = models.CharField(max_length=1, choices=SEASONS, verbose_name="Сезонность")
    load_index = models.IntegerField(
        verbose_name="Индекс нагрузки", blank=True, null=True
    )
    speed_rating = models.CharField(
        max_length=3, verbose_name="Индекс скорости", blank=True, null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Скидка, %", default=0.0
    )
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена со скидкой",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    image = models.ImageField(
        upload_to="tires/", verbose_name="Изображение", blank=True, null=True
    )
    feedback = models.URLField(
        max_length=255, verbose_name="Отзывы", blank=True, null=True
    )
    image_telegram_id = models.CharField(
        max_length=255, verbose_name="ID изображения в Telegram", blank=True, null=True
    )

    def __str__(self):
        return f"{self.brand} {self.width}/{self.height}R{self.diameter} {self.season} {self.price} руб."

    class Meta:
        verbose_name = "Шина"
        verbose_name_plural = "Шины"
        db_table = "tires"
