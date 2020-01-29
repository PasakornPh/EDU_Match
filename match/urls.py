from django.urls import path,include

from . import views

app_name = 'match'
urlpatterns = [
    # ex: /match/
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('account/',include('django.contrib.auth.urls')),
    path('profile/', views.profile,name='profile'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('clean_model/', views.clean_model, name='clean'),
    path('search/', views.searching, name='search'),

]