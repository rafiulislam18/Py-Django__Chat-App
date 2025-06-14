from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ChatmessageCreateForm


@login_required
def chat_view(request):
    chat_group = ChatGroup.objects.get_or_create(group_name='public-chat')[0]
    chatroom_name = chat_group.group_name
    chat_messages = chat_group.chat_messages.all()[:30]  # Fetch the last 30 messages
    form = ChatmessageCreateForm()

    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message': message,
                'user': request.user,
            }
            return render(request, 'rtchat/partials/chat_message_p.html', context)

    context = {
        'chatroom_name': chatroom_name,
        'chat_messages': chat_messages,
        'form': form,
    }
    return render(request, 'rtchat/chat.html', context)
