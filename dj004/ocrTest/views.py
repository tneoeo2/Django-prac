from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post

##후에 api로 ocr 결과 받아주는걸로 변경(사진 저장X)
def index(request):
  if request.method =="POST":
    print("POST request")
    if request.FILES['mainphoto']:
      print("FILES request")
      new_photo = Post.objects.create(
        # postname=request.POST['photoname'],
        mainphoto=request.FILES['mainphoto']
      )
      print("image: ", request.FILES['mainphoto'])
  else:
    return render(request,'ocrTest/index.html')
  return render(request, 'ocrTest/index.html', {'mainphoto': request.FILES['mainphoto']})