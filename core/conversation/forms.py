from django.forms import ModelForm

from .models import Conversation, ConversationMessage


class ConversationForm(ModelForm):
    class Meta:
        model = ConversationMessage
        fields = [
            "content",
        ]
