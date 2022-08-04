from django import views
from django.urls import path
from . import views

#이미지 업로드
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mysite'

urlpatterns = [
       path('', views.index, name='index'),
      #  path('posts/', views.ListView.as_view(), name='posts'),
] 




##이미지 url 설정 (MEDIA_URL로 들어오는 요청에 대해 MEDIA_ROOT 경로 탐색)
if settings.DEBUG:   #settings.DEBUG가 false 일시 빈리스트를 반환(명시적 표시를 위해 작성)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #runserver명령을 통해 구동하는 개발서버에서는 media파일 자동으로 서빙해주지않음
