from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class human(models.Model):

    name = models.CharField(max_length=211111111111)
    subject = models.ManyToManyField('Subject')
    wantmatch = models.ManyToManyField('Wantmatch')
    matched = models.ManyToManyField('Matched')
    tutor = models.ManyToManyField('Tutor')
    student = models.ManyToManyField('Student')
    def __str__(self):
        return self.name


class Subject(models.Model):

    name = models.CharField(max_length=211111111111)

    def __str__(self):
        return self.name

class Wantmatch(models.Model):

    name = models.CharField(max_length=211111111111)

    def __str__(self):
        return self.name
class Matched(models.Model):

    name = models.CharField(max_length=211111111111)

    def __str__(self):
        return self.name
class Tutor(models.Model):

    name = models.CharField(max_length=211111111111)

    def __str__(self):
        return self.name
class Student(models.Model):

    name = models.CharField(max_length=211111111111)

    def __str__(self):
        return self.name

class chatlog(models.Model):
    chatroom=models.CharField(max_length=211111111111)
    chatlo=models.CharField(max_length=2111111111111)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'