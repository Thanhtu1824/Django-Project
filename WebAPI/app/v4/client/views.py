from app.models import Client
from app.v4.client.serializers import ClientV4Serializers
from rest_framework import generics


class ClientListCreateApiView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientV4Serializers

class ClientRetriveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientV4Serializers