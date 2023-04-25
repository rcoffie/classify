from django.forms import ModelForm

from .models import ConversationMessage


class ConversationForm(ModelForm):
    class Meta:
        model = ConversationMessage
        fields = [
            "content",
        ]
