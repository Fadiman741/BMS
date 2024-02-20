from rest_framework import serializers
from .models import User, Menu, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "datecreated",
            "dateofbirth",
            "role",
            "status",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}


class MenuSerialiazer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Menu
        fields = [
            "id",
            "user",
            "menu_name",
            "description",
            "price",
            "category",
            "tags",
        ]

    def __str__(self):
        return self.user


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = MenuSerialiazer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "items",
            "status",
            "order_number",
            "created_at",
            "updated_at",
        ]
