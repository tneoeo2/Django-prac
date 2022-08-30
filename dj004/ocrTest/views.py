from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.urls import resolve
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import  Post, Ranking
from django.views import generic
from .semi_crawler import *

import datetime
import requests
import json


class ImgView(generic.ListView):
  model = Post
  
  template_name = 'ocrTest/imglist.html'     #템플릿 파일 위치 지정
  context_object_name = 'images'      #템플릿파일로 넘겨주는 객체리스트 이름지정 : html파일에서 설정한 이름으로 객체를 가져올 수 있다..!!
  paginate_by: 5      #한페이지에 보여줄 객체의 개수   (페이징)
  
def ranklist(request):
  date_list = list(Ranking.objects.dates("pub_date", "day"))
  
  return render(request, 'ocrTest/ranklist.html',{'date_list':date_list})
  

# #* 오늘 크롤링한 랭킹 데이터만 보여준다.
# class RankingDetailView(generic.DetailView):  
#   model = Ranking
  
#   template_name = 'ocrTest/rankdetail.html'
  
  
#   def get_ranking_queryset(self):         #해당날짜의 최신 50개 정보(50위까지) 가져오기 
#     # date : 2022-08-06 형식
#     print("TESTESETESTESTESTSETESTESETESTESTESTSETESTESETESTESTESTSE")
#     current_url = resolve(self.request.path_info).url_name
    
#     print("date : ",current_url)
#     date = current_url.split("/")
#     year = date[0]
#     month = date[1]
#     day = date[2]
  
#     t_date = datetime.date(year, month, day)
#     ranking_list = Ranking.objects.exclude(
#         pub_date = t_date
#         ).order_by('pub_date')[:50]
    
#     return  ranking_list
      
#* 오늘 크롤링한 랭킹 데이터만 보여준다.
def rankdetail(request, year, month, date):  
  print("TESTESETESTESTESTSETESTESETESTESTESTSETESTESETESTESTESTSE", year, month, date)
  model = Ranking
  
  #해당날짜의 최신 50개 정보(50위까지) 가져오기 
  # date : 2022-08-06 형식
  
  # print("date : ",current_url)
  # date = current_url.split("/")
  
  year = int(year)
  month = int(month)
  date = int(date)

  t_date = datetime.date(year, month, date)
  
  print("날짜 확인 :   ", t_date)
  
  ranking_list = reversed(Ranking.objects.filter(
      pub_date__startswith = t_date
      ).order_by("-pub_date")[:50])       #내림차순으로 정렬
  
  print("ranking_list : ", ranking_list)
  
  return render(request,  'ocrTest/rankdetail.html', {"ranking_list" : ranking_list})
      

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
      
        return render(request, 'ocrTest/ocr.html', {'mainphoto':new_photo})
      
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
    return render(request,'ocrTest/ocr.html')
  
  return render(request, 'ocrTest/ocr.html', {'mainphoto': request.FILES['file']})

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
    return render(request, 'ocrTest/ocr.html', {'ocr-result' : ocr_res})
  
  
  return render(request, 'ocrTest/ocr.html')
        

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
    
    
  
def index(request):
  return render(request, 'index.html')


# def login(request):
#   if request.method == 'POST':
    
#     return render(request, 'ocrTest/index.html')
    
#   else :    #get request시 
    
#     return render(request, 'ocrTest/login.html')
    
    
    

def signup(request):
  return render(request, 'ocrTest/signup.html')
  