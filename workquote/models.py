from django.db import models
from django.contrib.auth.models import User

class Workquote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.IntegerField()

    def __str__(self):
        return (self.user.username + ' | ' + str(self.quote))
    

class WorkJournal(models.Model):
    works = models.ManyToManyField(Workquote)
