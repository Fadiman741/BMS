from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
import uuid


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    dateofbirth = models.DateTimeField(null=True)
    #     profile_pic = models.ImageField(upload_to="profile_images/", null=True)
    role = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.email


class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True)
    tags = models.CharField(max_length=255, null=True)
    #     image = models.ImageField(upload_to="menu_images/", null=True)

    def __str__(self):
        return self.menu_name


def generate_order_number():
    return str(uuid.uuid4().hex[:6])


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu)
    status = models.CharField(
        max_length=10, choices=[("Open", "Open"), ("Closed", "Closed")], default="Open"
    )
    order_number = models.CharField(
        max_length=6, default=generate_order_number, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
