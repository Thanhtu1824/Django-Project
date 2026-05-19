from app.models import Product
from app.v4.product.serializers import ProductSerializers
from app.filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

class ProductRetriveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers