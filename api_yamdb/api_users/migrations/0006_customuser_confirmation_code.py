# Generated by Django 3.2 on 2024-02-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0005_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
