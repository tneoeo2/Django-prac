from email.mime import image
from django.db import models

# Create your models here.
class Post(models.Model):
  mainphoto = models.ImageField(blank=True, null=True, upload_to='')  
  photoname = models.CharField(max_length=50)

  def __str__(self):
    return self.photoname  

class Ranking(models.Model):
  pub_date = models.DateTimeField("data published...")
  title = models.CharField(max_length=100)
  image = models.ImageField(blank=True, null=True, upload_to='rank')
  start_date = models.DateField()         #시작 날짜
  end_date = models.DateField()           #끝 날짜
  place = models.CharField(max_length=30)
  ranking = models.CharField(max_length=10)
  
  def __str__(self):
    return self.title
  
  
