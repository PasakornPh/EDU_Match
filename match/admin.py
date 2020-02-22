
from django.contrib import admin

from .models import human,Subject,Wantmatch,Matched,chatlog,Profile,Student,Tutor,Review

admin.site.register(chatlog)
admin.site.register(human)
admin.site.register(Tutor)
admin.site.register(Wantmatch)
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Review)