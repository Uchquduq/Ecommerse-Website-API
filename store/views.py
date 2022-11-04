from rest_framework.viewsets import ModelViewSet
from store.serializers import *
from store.models import Product, Collection


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count("product"))
    serializer_class = CollectionSerializer
