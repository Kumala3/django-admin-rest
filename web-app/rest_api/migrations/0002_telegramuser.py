# Generated by Django 5.0.2 on 2024-03-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True, verbose_name='ID пользователя')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Username пользователя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия пользователя')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]