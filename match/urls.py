from django.urls import path,include
from match.views import SignUpView , ProfileView
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = 'match'
urlpatterns = [
    # ex: /match/
    path('chat/', include('chat.urls')),
    path('', views.home, name='home'),
    path('signup/',views.SignUpView, name='SignUpView'),
    path('profile/', views.ProfileView, name='ProfileView'),
    path('view_profile/<str:name>', views.view_other_profile, name='view_profile'),
    path('view_profile_R/<str:name>', views.view_r_profile, name='view_profile_R'),
    path('friendmatched/', views.friendmatched, name='friendmatched'),
    path('friendprofile/<str:name>', views.friendprofile, name='friendprofile'),
    path('unmatched/<str:name>', views.unfriendmatched, name='unmatched'),
    path('acceptmatch/<str:name>', views.acceptmatch, name='acceptM'),
    path('declinematch/<str:name>', views.declinematch, name='declineM'),
    path('matching/<str:name>', views.matching, name='matching'),
    path('request_match/', views.request_match, name='request_match'),
    path('unmatching/<str:name>', views.unmatching, name='unmatching'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('profile_add_subject/', views.profile_add_subject,name='profile_add_subject'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('clean_model/', views.clean_model, name='clean'),
    path('search/', views.searching, name='search'),
    path('accounts/change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change_password.html',
            success_url='/accounts/change_password/done'
        ),
        name='change_password'
    ),
    path('accounts/change_password/done', views.change_password_done, name='change_password_done'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
#path('signup/',SignUpView.as_view(), name='signup'),
