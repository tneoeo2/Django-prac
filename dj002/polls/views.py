from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.template import loader
# from django.http import Http404

from .models import Choice, Question

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
  question = get_object_or_404(Question, pk=question_id)

  return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):  
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)  
  try:
    #request.POST는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 객체
    selected_choice = question.choice_set.get(pk=request.POST['choice'])   #request.POST['choice']: 선택된 설문의 ID를 문자열로 반환
  except (KeyError, Choice.DoesNotExist):   #choice 없을 시 keyError 발생
    #질문폼 다시 보여주기
    return render(request, 'polls/detail.html', {
      'question':question,
      'error_message': "You didn't select a choice.",
      })
  else:
    selected_choice.votes += 1    #설문자 수 증가
    selected_choice.save()
    
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  #reverse: view함수에서 URL 하드코딩하지 않도록 도와줌: 제어를 전달하기 원하는 뷰 이름 URL패턴 변수부분조합하여 가리킴
                                                                                #'/polls/<int:question.id>/results/'
    
                  