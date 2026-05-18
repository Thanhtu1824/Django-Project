from django.urls import path

from app.v1.client.views import client_list, client_detail
from app.v1.post.views import post_list, post_detail

urlpatterns = [
    path('client', client_list),
    path('client/<pk>', client_detail),
    path('post', post_list),
    path('post/<pk>', post_detail)
]
