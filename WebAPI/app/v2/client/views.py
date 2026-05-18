from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models import Client
from django.http import Http404

from .serializers import ClientV2Serializers

class ClientList(APIView):
     
    permission_classes=([IsAuthenticated])

    def get(sefl, request):
        print(request.user)
        print(request.auth)
        clients = Client.objects.all()

        serializer = ClientV2Serializers(clients, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(sefl, request):
        serializer = ClientV2Serializers(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):

    def get_object(sefl, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404
        
    def get(sefl, request, pk):
        client = sefl.get_object(pk)

        serializer = ClientV2Serializers(client)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def put(sefl, request, pk):
        client = sefl.get_object(pk)
        serializer = ClientV2Serializers(client,data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(sefl, request, pk):
        client = sefl.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
