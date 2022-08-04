from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post, Comment, Member, Photo
# Create your views here.

def index(request):
  return  render(request, 'mysite/index.html')
  
class ListView(generic.ListView):
  model = Post
  template_name = "mysite/post_list.html"
  
  