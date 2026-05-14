from django.urls import include, path

from mysite import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tinymce/", include("tinymce.urls")),
    path("article/<slug:slug>/", views.article_detail, name="article_detail"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("subcategory/<slug:slug>/", views.subcategory_detail, name="subcategory_detail"),
]
