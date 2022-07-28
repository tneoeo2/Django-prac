from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('blog/',  blog),
    #URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>', posting, name='posting'),
]