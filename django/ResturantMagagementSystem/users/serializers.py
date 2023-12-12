from rest_framework import serializers
from .models import (
    User,
)  # Assuming your models are in the same directory or you have proper import


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "username",
            "address",
            "role",
            "created_at",
            "updated_at",
            "contact_number",
            "email",
            "date_of_birth",
            "status",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}
