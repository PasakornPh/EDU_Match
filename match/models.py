from django.db import models

# Create your models here.
class human(models.Model):

    name = models.CharField(max_length=211111111111)
    subject = models.ManyToManyField('Subject')
    wantmatch = models.ManyToManyField('Wantmatch')
    matched = models.ManyToManyField('Matched')
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

class chatlog(models.Model):
    chatroom=models.CharField(max_length=211111111111)
    chatlo=models.CharField(max_length=2111111111111)