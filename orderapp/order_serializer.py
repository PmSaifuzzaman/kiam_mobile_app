# order_serializer.py
from rest_framework import serializers
from .models import Order
from .serializers import OrderItemSerializer  # Import OrderItemSerializer from serializers module

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
