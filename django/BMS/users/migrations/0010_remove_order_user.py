# Generated by Django 5.0 on 2024-02-26 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_menu_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
