from rest_framework import serializers
from ...models import Client

class ClientV4Serializers(serializers.ModelSerializer):
    
     class Meta: 
        model = Client
        fields = '__all__'
        
