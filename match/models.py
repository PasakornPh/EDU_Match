from django.db import models

# Create your models here.
class human(models.Model):

    name = models.CharField(max_length=30)
    subject = models.ManyToManyField('Subject')

    def __str__(self):
        return self.name


class Subject(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name