from importlib.resources import contents
from django.shortcuts import render
from django.shortcuts import redirect
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

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Post.objects.create(       #Post.objects.create: 새로운 Post 모델 만들기  => 사용자가 전송한정보(postname, contents, mainphoto)바탕으로 새로운 글(post)모델 만드는 함수
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto']
            )
        else:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')                               #게시판 페이지로 redirect
    return render(request, 'main/new_post.html')
    