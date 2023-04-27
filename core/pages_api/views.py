from django.http import Http404
from drf_spectacular.utils import extend_schema
from item_engine.models import Item
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pages_api.serializers import CategorySerializer, ItemSerializer

# Create your views here.


class ListItem(APIView):
    @extend_schema(responses=ItemSerializer)
    def get(self, request, format=None):
        item = Item.objects.filter(is_sold=False)[0:3]
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    @extend_schema(responses=ItemSerializer)
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
