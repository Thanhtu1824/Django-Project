from app.models import Brand
from app.v4.brand.serializers import BrandSerializers
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class BrandListCreateApiView(generics.ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','created']

class BrandRetriveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers