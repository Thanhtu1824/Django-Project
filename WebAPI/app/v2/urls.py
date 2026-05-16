from django.urls import path
from app.v2.client.views import ClientDetail, ClientList, PostList, PostDetail

urlpatterns = [
    path('client', ClientList.as_view()),
    path('client/<int:pk>', ClientDetail.as_view()),
    path('post', PostList.as_view()),
    path('post/<int:pk>', PostDetail.as_view())
]
