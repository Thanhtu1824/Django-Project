from django.urls import path
from app.v4.client.views import ClientListCreateApiView, ClientRetriveUpdateDestroyApiView
from app.v4.post.views import PostListCreateApiView, PostRetriveUpdateDestroyApiView


urlpatterns = [
    path('client', ClientListCreateApiView.as_view()),
    path('client/<int:pk>',ClientRetriveUpdateDestroyApiView.as_view()),
    path('post', PostListCreateApiView.as_view()),
    path('post/<int:pk>',PostRetriveUpdateDestroyApiView.as_view())
]
