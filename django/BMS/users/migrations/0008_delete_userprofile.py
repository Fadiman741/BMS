# Generated by Django 5.0 on 2024-02-26 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
