from django.db import models

class NewsModel(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=300)
    newsText = models.TextField()

    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
class TabsModel(models.Model):
    url = models.URLField()
    pdf = models.URLField()
    name = models.CharField(max_length=300)
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name

class NoteModel(models.Model):
    url = models.URLField()
    pdf = models.URLField()
    name = models.CharField(max_length=300)
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name