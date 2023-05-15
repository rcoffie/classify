from conversation.models import Conversation, ConversationMessage
from rest_framework import serializers


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = [
            "id",
            "item",
            "members",
            "created_at",
            "modified_at",
        ]


class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessage
        fields = [
            "id",
            "conversation",
            "content",
            "created_at",
            "created_by",
        ]
