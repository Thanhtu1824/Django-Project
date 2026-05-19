import django_filters
from app.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    brand = django_filters.CharFilter(field_name='brand__name', lookup_expr='iexact')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    created_min = django_filters.DateTimeFilter(field_name='created', lookup_expr='date__gte')
    created_max = django_filters.DateTimeFilter(field_name='created', lookup_expr='date__lte')
    quantity = django_filters.NumberFilter(field_name='quantity', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = [
            'name', 
            'min_price', 
            'max_price', 
            'brand', 
            'category', 
            'created_min', 
            'created_max', 
            'quantity'
        ]