from rest_framework.serializers import ModelSerializer
from .models import Product, Cart, Order

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'