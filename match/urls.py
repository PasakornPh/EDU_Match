from django.urls import path,include
from match.views import SignUpView , ProfileView
from . import views

app_name = 'match'
urlpatterns = [
    # ex: /match/
    path('chat/', include('chat.urls')),
    path('', views.home, name='home'),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('view_profile/<str:name>', views.view_other_profile, name='view_profile'),
    path('account/',include('django.contrib.auth.urls')),
    path('profile_add_subject/', views.profile_add_subject,name='profile_add_subject'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('clean_model/', views.clean_model, name='clean'),
    path('search/', views.searching, name='search'),

]