from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateField('Publication Date')
    category = models.CharField(max_length=50)
    imageMain = models.ImageField(upload_to="images")
    imageAdditional = models.ImageField(upload_to='images',blank = True)
    text = models.CharField(max_length=1000)
    
class Recommendation(models.Model):
    ref_article = models.ForeignKey(Article, related_name ='article',blank=True,default="")
    recommendation = models.ForeignKey(Article, related_name= 'recommendation',blank=True,default="")
    timestamp = models.DateTimeField(default=timezone.now,blank=True)
