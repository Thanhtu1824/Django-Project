from app.models import Post
from app.v4.post.serializers import PostV4Serializers
from rest_framework import generics


class PostListCreateApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostV4Serializers

class PostRetriveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostV4Serializers