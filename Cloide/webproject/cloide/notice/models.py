from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    author = models.CharField(max_length=100, default="simple")

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:30]