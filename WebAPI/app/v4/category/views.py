from app.models import Category
from app.v4.category.serializers import CategorySerializers
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListCreateApiView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','created']

class CategoryRetriveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers