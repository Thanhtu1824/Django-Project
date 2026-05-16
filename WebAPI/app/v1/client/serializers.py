from rest_framework import serializers
from ...models import Client, Post

class ClientV1Serializers(serializers.ModelSerializer):
    
     class Meta: 
        model = Client
        fields = ['id', 'name', 'gender', 'active', 'created']

class PostV1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'