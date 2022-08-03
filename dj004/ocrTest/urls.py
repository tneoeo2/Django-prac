from django.urls import path
from .views import *

#이미지 업로드
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'),
]


##이미지 url 설정 (MEDIA_URL로 들어오는 요청에 대해 MEDIA_ROOT 경로 탐색)
if settings.DEBUG:   #settings.DEBUG가 false 일시 빈리스트를 반환(명시적 표시를 위해 작성)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #runserver명령을 통해 구동하는 개발서버에서는 media파일 자동으로 서빙해주지않음