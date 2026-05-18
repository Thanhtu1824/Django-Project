from django.urls import path
from app.v3.client.views import ClientList, ClientDetail
from app.v3.post.views import PostList, PostDetail


urlpatterns = [
    path('client', ClientList.as_view()),
    path('client/<int:pk>',ClientDetail.as_view()),
    path('post', PostList.as_view()),
    path('post/<int:pk>',PostDetail.as_view())
]
