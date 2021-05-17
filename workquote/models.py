from django.db import models
from django.contrib.auth.models import User

class Workquote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.IntegerField()
    date = models.DateField(default='2001-12-12')
    description = models.TextField(default='Сложная работа')

    def __str__(self):
        return (self.user.username + ' | ' + str(self.quote) + ' # ' + str(self.date))
    