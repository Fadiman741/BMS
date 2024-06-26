# Generated by Django 5.0 on 2024-02-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('period', models.CharField(blank=True, max_length=50)),
                ('contacts', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('action', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
