from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from match.models import human,Subject

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
                'new_subject': request.POST.get('item_subject', ''),'count' : count
            })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match:home')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{
        'form' : form
    })

def profile(request):
    return render(request, 'profile.html')

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