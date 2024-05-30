# Generated by Django 3.2 on 2024-02-18 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0011_remove_customuser_unique_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=255, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('user', 'Аутентифицированный пользователь'), ('moderator', 'Модератор')], default='user', max_length=30, verbose_name='Роль'),
        ),
    ]