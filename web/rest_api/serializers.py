from rest_framework import serializers
from .models import (
    TelegramUser,
    Diameter,
    Width,
    Height,
    Tire,
)

from admin_panel.models import CartItem, Order, OrderItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = "__all__"


class DiameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diameter
        fields = "__all__"


class WidthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Width
        fields = "__all__"


class HeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Height
        fields = "__all__"


class TireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tire
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

    def create(self, validated_data):
        return CartItem.objects.create(**validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
