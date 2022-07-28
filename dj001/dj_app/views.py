from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')   #띄울 페이지 경로

def blog(request):
    return render(request, 'main/blog.html')
