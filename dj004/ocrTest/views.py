from urllib import response
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import  Ranking

from .models import Post
from .semi_crawler import *

import requests
import json

##후에 api로 ocr 결과 받아주는걸로 변경(사진 저장X)
def ocr(request):
  print("request",request)
  # print("request_dir",dir(request))
  print("request.method: ", request.method)
  if request.method =="POST":
      print("POST request")
      try:
        new_photo = request.POST['file']
        print("new_photo-------",new_photo)
      
        return render(request, 'ocrTest/index.html', {'mainphoto':new_photo})
      
      except:
  
        print("post-------",request.POST)
        # data = request.body
        # print("data-------",data)
        
        if request.FILES['file']:
          print("FILES request")
          new_photo = Post.objects.create(
            # postname=request.POST['photoname'],
            mainphoto=request.FILES['file']
          )
          print("image: ", request.FILES['file'])
  else:
    return render(request,'ocrTest/index.html')
  
  return render(request, 'ocrTest/index.html', {'mainphoto': request.FILES['file']})

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

def ocrAPI(request):
  url = "http://61.72.55.130:8999/ocr/imgUploadMulti"
  if request.method =="POST":
    form_data = request.POST
    print('form_data:', form_data)
    dict_data = form_data.dict()
    print('dict_data:', dict_data)
    json_data = json.dumps(dict_data)
    print('json_data_af:', json_data)
    
    file = dict_data['file']     #이미지데이터보내기(인코딩)
    ocrmode = dict_data['ocrmode']
    metaId = dict_data['metaId']
    docModelId = dict_data['docModelId']
    
    print("file : %s, ocrmode : %s" % (file, ocrmode))
    ocr_res = requests.post(url, json=json_data)
    print("ocr_res : ", ocr_res)
    header = {}
    return render(request, 'ocrTest/index.html', {'ocr-result' : ocr_res})
  
  
  return render(request, 'ocrTest/index.html')
        

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
    