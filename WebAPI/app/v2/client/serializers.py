from rest_framework import serializers
from ...models import Client, Post

class ClientV2Serializers(serializers.ModelSerializer):
    
     class Meta: 
        model = Client
        fields = '__all__'
        
class PostV2Serializers(serializers.ModelSerializer):
    
      class Meta:
         model = Post
         fields = '__all__'