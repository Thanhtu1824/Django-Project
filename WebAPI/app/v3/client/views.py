from app.models import Client
from app.v3.client.serializers import ClientV3Serializers
from rest_framework import mixins
from rest_framework import generics


class ClientList(mixins.ListModelMixin, 
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientV3Serializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ClientDetail(mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin, 
                   mixins.DestroyModelMixin, 
                   generics.GenericAPIView):
    
    queryset = Client.objects.all()
    serializer_class = ClientV3Serializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    