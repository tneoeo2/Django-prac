from msilib.schema import PublishComponent
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import  Ranking

from .models import Post
from .semi_crawler import *

import json

##후에 api로 ocr 결과 받아주는걸로 변경(사진 저장X)
def ocr(request):
  print("request",request)
  # print("request_dir",dir(request))
  
  if request.method =="POST":
      print("POST request")
      try:
        new_photo = request.POST['mainphoto']
        print("new_photo-------",new_photo)
      
        return render(request, 'ocrTest/index.html', {'mainphoto':new_photo})
      
      except:
  
        print("post-------",request.POST)
        # data = request.body
        # print("data-------",data)
        
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

# def ocr(request):
  
#   return render(request, 'ocrTest/rank.html')
        

# @csrf_exempt
def save(request):
  print("save-------------------------")
  if request.method == "POST":
    data = request.body
    json_data = json.loads(data)
    
    print(json_data)
    data_len = len(list(json_data.keys()))
    for i in range(data_len):
      idx = str(i)
      date = json_data[idx]['date'].replace('.', '-')
      
      new_data = Ranking.objects.create(
        pub_date = timezone.now()
        ,title = json_data[idx]['title']
        ,image = json_data[idx]['image']
        ,place = json_data[idx]['place']
        ,start_date = date.split('~')[0]
        ,end_date = date.split('~')[1]
        ,ranking = json_data[idx]['ranking']
      )
      
    print("POST 테스트입니다!!!!!!!!!!!!!!")
    return redirect('/rank/')
    
  return render(request, 'ocrTest/rank.html')
    