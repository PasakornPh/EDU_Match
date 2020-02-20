
from django.contrib import admin

from .models import human,Subject,Wantmatch,Matched,chatlog,Profile

admin.site.register(chatlog)
admin.site.register(Profile)