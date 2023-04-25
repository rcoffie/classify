from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework import status 
from item_engine.models import Item
from pages_api.serializers import ItemSerializer
from django.http import Http404
# Create your views here.


class ListItem(APIView):

    def get(self, request, format=None):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
   def get_object(self,pk):
    try:
        return Item.objects.get(pk=pk)
    except Item.objects.DoesNotExist:
        raise Http404

   def get(self, request, pk, format=None):
    item = self.get_object(pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

   def put(self, request, pk, format=None):
    item = self.get_object(pk)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, pk, format=None):
    item = self.get_object(pk)
    item.delete()
    return Response(status=status.HTTP_200_NO_CONTENT)