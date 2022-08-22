from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post
from .semi_crawler import *

import json

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

def rank(request):
  
  return render(request, 'ocrTest/rank.html')


def get_rank(request):
  try:
    driver = run()
    ranking_info= run_browser(driver)
    json_rank_info = json.dumps(ranking_info, indent=4, ensure_ascii= False)
    print(json_rank_info)
  except(Exception)  :
    print("except-------------------------")
    return render(request, 'ocrTest/rank.html', {'ranking_info': "ERROR_ERROR_ERROR"})
  print("http Response=---------")
  return HttpResponse(json_rank_info, content_type = "application/json")