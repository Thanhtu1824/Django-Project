from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Post
from django.http import Http404

from .serializers import PostV2Serializers


class PostList(APIView):

    def get(sefl, request):
        posts = Post.objects.all()

        serializer = PostV2Serializers(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(sefl, request):
        serializer = PostV2Serializers(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):

    def get_object(sefl, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    def get(sefl, request, pk):

        post = sefl.get_object(pk)

        serializer = PostV2Serializers(post)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(sefl, request, pk):
        post = sefl.get_object(pk)
        serializer = PostV2Serializers(post,data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(sefl, requet, pk):
        post=sefl.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)