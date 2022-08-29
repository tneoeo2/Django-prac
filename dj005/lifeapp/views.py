from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):     #request : 요청과 관련된 객체(이름 바꿔도 가능하나 관습적으로 request 사용)
  return HttpResponse("Welcome!!")

def create(request):
  return HttpResponse("Create")
  
def read(request, id):
  return HttpResponse("Read!" + id)

