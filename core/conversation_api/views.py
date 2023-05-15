from django.shortcuts import render
from django.http import Http404
from conversation.models import Conversation, ConversationMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from conversation_api.serializers import ConversationSerializer, ConversationMessageSerializer
from item_engine.models import Item
from rest_framework.permissions import IsAuthenticated




class ConversationList(APIView):
    def get(self, request, format=None):
        conversations = Conversation.objects.all() 
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConversationDetails(APIView):
    def get_object(self, pk):
        try:
            return Conversation.objects.get(pk=pk)
        except Conversation.DoesNoExist:
            raise Http404 

    def get(self, request, pk, format=None):
        conversation = sef.get_object(pk)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        conversation = self.get_object(pk)
        serializer = ConversationSerializer(conversation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        conversation = self.get_object(pk)
        conversation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    