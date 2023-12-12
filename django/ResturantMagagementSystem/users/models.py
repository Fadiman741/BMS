from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(null=True, max_length=255)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    address = models.TextField(null=True, max_length=255)
    role = models.CharField(null=True, max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact_number = models.CharField(null=True, max_length=15)
    email = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField(null=True)
    status = models.CharField(null=True, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    def __str__(self):
        return self.first_name
