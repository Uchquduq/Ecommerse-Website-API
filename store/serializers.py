from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )

    class Meta:
        model = Product
        fields = ["id", "title", "price", "collection", "price_with_tax"]

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

