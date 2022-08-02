from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.template import loader
# from django.http import Http404

from .models import Choice, Question

##Generic으로 변경
##ListView : 객체 목록 표시     -> <app name>/<model name>_list.html 템플릿 사용 
##DetailView : 특정 개체 유형 세부 정보 페이지 표시   -> <app name>/<model name>_detail.html 템플릿을 사용
class IndexView(generic.ListView):    
  template_name = 'polls/index.html'        #기본이름 양식(_list)대신 다른 이름 사용할 때 사용
  context_object_name = 'latest_question_list'    #자동으로 생성되는 컨텍스트 변수 덮어쓰기(question_list 덮어쓰기)

  def get_queryset(self):
    #timeznoe.now 보다 pub_date가 작거나 같은 Question을 포함하는 queryset반환하여 정렬(5개)
    return Question.objects.filter(
      pub_date__lte = timezone.now()).order_by('-pub_date')[:5]
    # return Question.objects.order_by('-pub_date')[:5]     #최신순으로 정렬 5개의 -> 최신 5개 질문 뽑기
  
class DetailView(generic.DetailView):
  model = Question
  template_name = "polls/detail.html" 
  
class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'
  
def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)      #pk가 없을 시 404페이지를 반환한다.
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
    
                  