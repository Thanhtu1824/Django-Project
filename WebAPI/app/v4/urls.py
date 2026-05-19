from django.urls import path
from app.v4.product.views import ProductListCreateApiView, ProductRetriveUpdateDestroyApiView
from app.v4.brand.views import BrandListCreateApiView, BrandListCreateApiView
from app.v4.category.views import CategoryListCreateApiView, CategoryListCreateApiView


urlpatterns = [
    path('product', ProductListCreateApiView.as_view()),
    path('product/<int:pk>',ProductRetriveUpdateDestroyApiView.as_view()),
    path('brand', BrandListCreateApiView.as_view()),
    path('brand/<int:pk>',BrandListCreateApiView.as_view()),
    path('category', CategoryListCreateApiView.as_view()),
    path('category/<int:pk>',CategoryListCreateApiView.as_view()),
]
