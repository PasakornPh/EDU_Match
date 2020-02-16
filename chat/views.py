from django.shortcuts import render
from match.models import chatlog
from django.contrib.auth.models import User
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    chat=chatlog.objects.get(chatroom=room_name)
    splited=str(chat.chatlo).split('\n')
    sum=''
    for i in splited:
        if request.user.username in i:
            sum+='\t\t\t\t\t\t\t\t\t'+i+'\n'
        else:
            sum+=i+'\n'

    return render(request, 'chat/room.html', {
        'room_name': room_name,'old_message':sum
    })