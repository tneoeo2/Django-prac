from django.db import models

# Create your models here.
class Post(models.Model):
  mainphoto = models.ImageField(blank=True, null=True, upload_to='')  
  photoname = models.CharField(max_length=50)

  def __str__(self):
    return self.photoname
