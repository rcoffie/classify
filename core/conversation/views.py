from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation, ConversationMessage
from .forms import ConversationForm
from item_engine.models import Item
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def new_conversation(request, id):
    item = get_object_or_404(Item, id=id)

    if item.created_by == request.user:
        return redirect('dashboard')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        pass 

    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user 
            conversation_message.save()

            return redirect('item_detail', id=item.id)
    else:
        form = ConversationForm() 

    return render(request, 'conversation/new.html',{
            'form':form,
        } )
