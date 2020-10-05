from django.db import models
# Create your models here.
class Magazine(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    business_number = models.IntegerField()
    style = models.IntegerField()  
    kind = models.IntegerField()
    url = models.TextField('url')
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title