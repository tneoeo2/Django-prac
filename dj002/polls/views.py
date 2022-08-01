from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]     #최신순으로 정렬 5개의 -> 최신 5개 질문 뽑기
  # template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list': latest_question_list,
  }
  
  return render(request, 'polls/index.html', context)    #request, 템플릿 이름 , context(사전형 객체: 선택적 인수)
  # return HttpResponse(template.render(context, request)) #
  # return HttpResponse("Hello, world! Your're at the polls index.")

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):  
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
                      