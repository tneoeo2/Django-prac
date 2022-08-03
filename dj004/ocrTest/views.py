from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post


def index(request):
  
  return render(request, 'ocrTest/index.html')