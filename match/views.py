from django.http import HttpResponse
from django.shortcuts import render

from match.models import human,Subject


def edit_profile(request):

    return render(request, "profile.html",)

def home_page(request):
    if request.method == 'POST':
        firstsubject = Subject(name=request.POST.get('item_subject',''))
        firstsubject.save()
        if not human.objects.filter(name='man').exists():
            User1 = human(name='man')
            User1.save()
        human.objects.get(name='man').subject.add(firstsubject)
        User1= human.objects.get(name='man')
        return render(request, 'home.html', {
                'User':User1,
            })
    else:
        return render(request, 'home.html',)

