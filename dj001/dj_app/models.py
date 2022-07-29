from distutils.command import upload
from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)          
    #upload_to : /media/upload_to에서 지정한 경로/파일명.확장자
    mainphoto = models.ImageField(blank=True, null=True, upload_to='')   #이미지 필드 생성  null:True(null값 허용), blank:True(입력없어도 됨)
    contents = models.TextField()
    
    def __str__(self):
        return self.postname
    
    

    
