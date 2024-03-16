# Generated by Django 5.0 on 2024-03-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('todo', 'Todo'), ('in_progress', 'In Progress'), ('done', 'Done')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(max_length=1000, unique=True),
        ),
    ]