from turtle import settiltangle
from django.urls import path
from .views import *

#이미지 업로드
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'),
    path('blog/',  blog),
    #URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>', posting, name='posting'),
    path('blog/new_post', new_post)
]


##이미지 url 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)