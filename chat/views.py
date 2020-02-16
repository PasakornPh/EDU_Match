from django.shortcuts import render
from match.models import chatlog
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    chat=chatlog.objects.get(chatroom=room_name)
    return render(request, 'chat/room.html', {
        'room_name': room_name,'old_message':chat.chatlo
    })