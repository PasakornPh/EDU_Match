from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from match.models import human,Subject,Matched,Wantmatch

from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView

from match.forms import SignUpForm , ProfileForm

def home(request):

    count = User.objects.count()
    username = None

    if request.user.is_authenticated:
        username = request.user.username
        if not human.objects.filter(name=username).exists():
            User1 = human(name=username)
            User1.save()
        currentu=human.objects.get(name=request.user.username)
        wantmatchcount=currentu.wantmatch.all().count
        return render(request, 'home.html', {
            'new_subject': request.POST.get('item_subject', ''), 'wantmatchcount': wantmatchcount
        })
    return render(request, 'home.html', {
                'new_subject': request.POST.get('item_subject', ''),'count' : count
            })

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/profile.html'

def request_match(request):
    Nosent="No one sent you a matching"
    User1= human.objects.get(name=request.user.username)
    if User1.wantmatch.all() :
        allwantmatch=User1.wantmatch.all()
        return render(request,"recievematch.html",{'allwantmatch': allwantmatch, 'count' : allwantmatch.count()})
    return render(request,"recievematch.html",{'Nosent': Nosent})

def friendmatched(request):
    User1=human.objects.get(name=request.user.username)
    User1.matched.all()
    Nomatched = "You didn't match anyone"
    User1 = human.objects.get(name=request.user.username)
    if User1.matched.all():
        allmatched = User1.matched.all()
        return render(request, "Friend_matched.html", {'allmatched': allmatched, 'count': allmatched.count()})
    return render(request, "Friend_matched.html", {'Nomatched': Nomatched})

def friendprofile(request,name):
    Selecteduser = User.objects.get_by_natural_key(name)
    username = Selecteduser.username
    return render(request, 'Friend_profile.html', {'username': username, 'firstname': Selecteduser.first_name
        , 'lastname': Selecteduser.last_name, 'email': Selecteduser.email, 'name': username})

def view_r_profile(request,name):
    Selecteduser = User.objects.get_by_natural_key(name)
    username = Selecteduser.username
    return render(request, 'recieve_profile.html', {'username': username, 'firstname': Selecteduser.first_name
        , 'lastname': Selecteduser.last_name, 'email': Selecteduser.email, 'name': username})

def view_other_profile(request,name):
    Selecteduser=User.objects.get_by_natural_key(name)
    username=Selecteduser.username
    User1= human.objects.get(name=name)
    if User1.wantmatch.filter(name=request.user.username):
        checked=1
        return render(request, 'other_profile.html',
                      {'username': username, 'firstname': Selecteduser.first_name, 'lastname': Selecteduser.last_name,
                       'email': Selecteduser.email, 'name': username ,'checked' : checked })
    else:
        return render(request, 'other_profile.html', {'username': username ,'firstname': Selecteduser.first_name
            ,'lastname': Selecteduser.last_name, 'email':Selecteduser.email , 'name': username })

def unfriendmatched(request,name):
    User1 = human.objects.get(name=request.user.username)
    Selunmatched=User1.matched.get(name=name)
    Selunmatched.delete()

    User2 = human.objects.get(name=name)
    Selunmatched2=User2.matched.get(name=request.user.username)
    Selunmatched2.delete()


    User1.matched.all()
    Nomatched = "You didn't match anyone"
    User1 = human.objects.get(name=request.user.username)
    if User1.matched.all():
        allmatched = User1.matched.all()
        return render(request, "Friend_matched.html", {'allmatched': allmatched, 'count': allmatched.count()})
    return render(request, "Friend_matched.html", {'Nomatched': Nomatched})

def acceptmatch(request,name):
    Selecteduser = User.objects.get_by_natural_key(request.user.username)
    username = Selecteduser.username
    User1 = human.objects.get(name=request.user.username)
    # User1= human.objects.get(pk=1).delete()
    User2 = get_object_or_404(human, name=request.user.username)
    User3 = get_object_or_404(human, name=name)
    selected_unmatch = User2.wantmatch.get(name=name)
    selected_unmatch.delete()
    if not Matched.objects.filter(name=name).exists():
        firstsubject = Matched(name=name)
        firstsubject.save()
    if not Matched.objects.filter(name=request.user.username).exists():
        firstsubject = Matched(name=request.user.username)
        firstsubject.save()
    fmatched=Matched.objects.get(name=name)
    fmatched2=Matched.objects.get(name=request.user.username)
    User2.matched.add(fmatched)
    User3.matched.add(fmatched2)
    Nosent = "No one sent you a matching"
    User1 = human.objects.get(name=request.user.username)
    if User1.wantmatch.all():
        allwantmatch = User1.wantmatch.all()
        return render(request, "recievematch.html", {'allwantmatch': allwantmatch, 'count': allwantmatch.count()})
    return render(request, "recievematch.html", {'Nosent': Nosent})

def declinematch(request,name):
    Selecteduser = User.objects.get_by_natural_key(request.user.username)
    username = Selecteduser.username
    User1 = human.objects.get(name=request.user.username)
    # User1= human.objects.get(pk=1).delete()
    User2 = get_object_or_404(human, name=request.user.username)
    selected_unmatch = User2.wantmatch.get(name=name)
    selected_unmatch.delete()
    Nosent = "No one sent you a matching"
    User1 = human.objects.get(name=request.user.username)
    if User1.wantmatch.all():
        allwantmatch = User1.wantmatch.all()
        return render(request, "recievematch.html", {'allwantmatch': allwantmatch, 'count': allwantmatch.count()})
    return render(request, "recievematch.html", {'Nosent': Nosent})

def searching(request):
    count = User.objects.count()
    if not Subject.objects.filter(name=request.POST.get('item_subject2', '')).exists():
        Noresult = 'No users were found matching'
        return render(request, 'home.html', {'Noresult': Noresult,'count' : count})
    firstsubject = Subject.objects.get(name=request.POST.get('item_subject2', ''))
    first= firstsubject.human_set.all().exclude(name=request.user.username)
    User1=human.objects.get(name=request.user.username)

    for matched in User1.matched.all():
        first= first.exclude(name=matched)

    #    fisubject.add(Subject)
    return render(request, 'home.html', {'usermatched': User1.matched.all(),'userins': first,'count': count})


def profile_add_subject(request):
    User1 = human.objects.get(name=request.user.username)
    return render(request, 'add_subject.html', {
        'User': User1,
    })

def matching(request,name):

    Selecteduser = User.objects.get_by_natural_key(name)
    username = Selecteduser.username
    if not Wantmatch.objects.filter(name=request.user.username ).exists():
        firstwm = Wantmatch(name=request.user.username)
        firstwm.save()
    fwantmatch = Wantmatch.objects.get(name=request.user.username)
    human.objects.get(name=name).wantmatch.add(fwantmatch)

    User1 = human.objects.get(name=name)
    if User1.wantmatch.filter(name=request.user.username):
        checked=User1.wantmatch.all().count()
        return render(request, 'other_profile.html',
                      {'username': username, 'firstname': Selecteduser.first_name, 'lastname': Selecteduser.last_name,
                       'email': Selecteduser.email, "checked": checked})
    return render(request, 'other_profile.html',
                  {'username': username, 'firstname': Selecteduser.first_name, 'lastname': Selecteduser.last_name,
                   'email': Selecteduser.email})


def unmatching(request,name):
    Selecteduser = User.objects.get_by_natural_key(name)
    username = Selecteduser.username
    User1 = human.objects.get(name=name)
    # User1= human.objects.get(pk=1).delete()
    User2 = get_object_or_404(human, name=name)
    selected_unmatch = User2.wantmatch.get(name=request.user.username)
    selected_unmatch.delete()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    checked=0

    return render(request, 'other_profile.html',
                  {'username': username, 'firstname': Selecteduser.first_name, 'lastname': Selecteduser.last_name,
                   'email': Selecteduser.email })

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
    return render(request, 'add_subject.html', {
        'User': User1,
    })

def clean_model(request):
    User1 = human.objects.get(name=request.user.username)
    #User1= human.objects.get(pk=1).delete()
    new_subject_list = request.POST.getlist('new_subject')
    if len(new_subject_list) == 0:
        # Redisplay the question voting form.

        return render(request, 'add_subject.html', {
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

        return render(request, 'add_subject.html', {'User':User1})

def change_password_done(request):
    return render(request, 'registration/change_password_done.html')