from decimal import Decimal
from django.db.models.aggregates import Count
from rest_framework import serializers
from store.models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    # products_count = serializers.SerializerMethodField(method_name='get_products_count')
    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Collection
        fields = ["id", "title", "products_count"]


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )

    class Meta:
        model = Product
        fields = ["id", "title", "price", "collection", "price_with_tax"]

    def calculate_tax(self, product: Product):
        return round(product.unit_price * Decimal(1.1), 2)

    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError("Password does not match")
    #     return data

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        instance.unit_price = validated_data.get("unit_price")
        instance.collection = validated_data.get("collection")
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "date", "name", "description"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)
