from app.models import Post
from app.v3.post.serializers import PostV3Serializers
from rest_framework import mixins
from rest_framework import generics


class PostList(mixins.ListModelMixin, 
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostV3Serializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class PostDetail(mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin, 
                   mixins.DestroyModelMixin, 
                   generics.GenericAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostV3Serializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    