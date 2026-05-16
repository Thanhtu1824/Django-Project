from django.urls import path, include

urlpatterns = [
    path('/',),
    path('tinymce/', include('tinymce.urls')),
]
