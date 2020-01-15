from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from match.models import human,Subject


def matching(request):

    return render(request, "home.html",)
def add_subject(request):
    firstsubject = Subject(name=request.POST.get('item_subject', ''))
    firstsubject.save()
    if not human.objects.filter(name='man').exists():
        User1 = human(name='man')
        User1.save()
    human.objects.get(name='man').subject.add(firstsubject)
    User1 = human.objects.get(name='man')
    return render(request, 'profile.html', {
        'User': User1,
    })
def home_page(request):
    return render(request, 'home.html',)

def profile(request):
    return render(request, 'profile.html')

def clean_model(request):
    User1 = human.objects.get(name='man')
    #User1= human.objects.get(pk=1).delete()
    new_subject_list = request.POST.getlist('new_subject')
    if len(new_subject_list) == 0:
        # Redisplay the question voting form.

        return render(request, 'profile.html', {
            'User': User1,
            'error_message': "You didn't select a subject.",
        })
    else:
        User2 = get_object_or_404(human, name='man')
        for index in new_subject_list:
            print(index)
            selected_subject = User2.subject.get(pk=index)

            selected_subject.delete()

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.

        return render(request, 'profile.html', {'User':User1})