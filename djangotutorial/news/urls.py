from django.urls import include, path

from mysite import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tinymce/", include("tinymce.urls")),
]
