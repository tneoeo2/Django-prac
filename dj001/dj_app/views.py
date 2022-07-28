from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')   #띄울 페이지 경로

def blog(request):
    #모든 post 가져와 postlist에 저장
    postlist = Post.objects.all()
    #blog.html dufEo 모든 포스트 postlist 같이 가져옴
    
    return render(request, 'main/blog.html', {'postlist': postlist})

def posting(request, pk):
    #게시글(Post)중 pk(Primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    #posting.html 페이지를 열 떄, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post': post})