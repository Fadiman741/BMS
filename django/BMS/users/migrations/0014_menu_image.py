# Generated by Django 5.0 on 2024-03-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_menu_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(null=True, upload_to='menu_images/'),
        ),
    ]