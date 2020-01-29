from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from match.models import human,Subject

def home(request):
    count = User.objects.count()
    username = None

    if request.user.is_authenticated:
        username = request.user.username
        if not human.objects.filter(name=username).exists():
            User1 = human(name=username)
            User1.save()
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


def searching(request):
    count = User.objects.count()
    userinsubject=[]
    if not Subject.objects.filter(name=request.POST.get('item_subject2', '')).exists():
        Noresult = 'No users were found matching'
        return render(request, 'home.html', {'Noresult': Noresult,'count' : count})
    firstsubject = Subject.objects.get(name=request.POST.get('item_subject2', ''))
    first= firstsubject.human_set.all().exclude(name=request.user.username)



    #    fisubject.add(Subject)
    return render(request, 'home.html', {'userins': first,'count': count})


def profile(request):
    User1 = human.objects.get(name=request.user.username)
    return render(request, 'profile.html', {
        'User': User1,
    })

def matching(request):
    return render(request, "home.html",)

def add_subject(request):
    if not Subject.objects.filter(name=request.POST.get('item_subject', '')).exists():
        firstsubject = Subject(name=request.POST.get('item_subject', ''))
        firstsubject.save()
    if not human.objects.filter(name=request.user.username).exists():
        User1 = human(name=request.user.username)
        User1.save()
    fsubject = Subject.objects.get(name=request.POST.get('item_subject', ''))
    human.objects.get(name=request.user.username).subject.add(fsubject)
    User1 = human.objects.get(name=request.user.username)
    return render(request, 'profile.html', {
        'User': User1,
    })

def clean_model(request):
    User1 = human.objects.get(name=request.user.username)
    #User1= human.objects.get(pk=1).delete()
    new_subject_list = request.POST.getlist('new_subject')
    if len(new_subject_list) == 0:
        # Redisplay the question voting form.

        return render(request, 'profile.html', {
            'User': User1,
            'error_message': "You didn't select a subject.",
        })
    else:
        User2 = get_object_or_404(human, name=request.user.username)
        for index in new_subject_list:
            print(index)
            selected_subject = User2.subject.get(pk=index)

            selected_subject.delete()

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.

        return render(request, 'profile.html', {'User':User1})