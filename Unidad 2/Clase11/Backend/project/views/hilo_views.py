from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer.hilo_serializer import HiloSerializers
from api.models.hilo import Hilo
from rest_framework import status
from django.http import Http404
    
class Hilo_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Hilo.objects.all()
        serializer = HiloSerializers(post, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = HiloSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Hilo_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Hilo.objects.get(pk=pk)
        except Hilo.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        try:
            hilo = Hilo.objects.get(pk=pk)
        except Hilo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = HiloSerializers(hilo)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        hilo = self.get_object(pk)
        serializer = Hilo(hilo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        hilo = self.get_object(pk)
        hilo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
