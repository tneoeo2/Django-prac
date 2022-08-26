from django.urls import path, re_path
from .views import *

#이미지 업로드
from django.conf.urls.static import static
from django.conf import settings

ap_name = 'ocrTest'      #app namespace 

urlpatterns = [
    # path('', index, name='index'),
    path('rank/', rank, name='rank'),
    path('get_rank/', get_rank, name='get_rank'),
    path('save/', save, name='save'),
    path('ocr/', ocr, name='ocr'),
    path('ocrAPI/', ocrAPI, name='ocrAPI'),
    path('imgs/', ImgView.as_view(), name='imgs'),
    path('rankinglist/', rankinglist, name='rankinglist'),
    # path(r'^(?P<year>[0-9]{4}/?P<month>[0-9]{2}/?P<date>[0-9]{2}/rankingdetail/', RankingDetailView.as_view(), name='rankingdetail'),
    path('rankingdetail/', rankingdetail, name='rankingdetail'),
]


##이미지 url 설정 (MEDIA_URL로 들어오는 요청에 대해 MEDIA_ROOT 경로 탐색)
if settings.DEBUG:   #settings.DEBUG가 false 일시 빈리스트를 반환(명시적 표시를 위해 작성)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #runserver명령을 통해 구동하는 개발서버에서는 media파일 자동으로 서빙해주지않음