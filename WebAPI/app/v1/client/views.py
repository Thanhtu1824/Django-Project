from http import client

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Client, Post
from app.v1.client.serializers import ClientV1Serializers, PostV1Serializers
# Create your views here.

@api_view(['GET','POST'])
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientV1Serializers(clients, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = ClientV1Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = ClientV1Serializers(client)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ClientV1Serializers(client, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
# POST

@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostV1Serializers(post, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = PostV1Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = PostV1Serializers(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostV1Serializers(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)