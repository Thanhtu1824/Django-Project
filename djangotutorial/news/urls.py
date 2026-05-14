from django.urls import include, path

from mysite import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tinymce/", include("tinymce.urls")),
    path("article/<slug:slug>/", views.article_detail, name="article_detail"),
]
