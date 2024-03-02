from django.db import models

# Create your models here.


class User(models.Model):
    telegram_id = models.IntegerField(verbose_name="ID пользователя", unique=True)
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
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'
        ordering = ('-created_at',)
