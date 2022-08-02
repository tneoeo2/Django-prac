import datetime
from urllib import response

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
# Create your tests here.

from .models import Question
  
def create_question(question_text, days):    #테스트 중 설문 생성하는 함수
  time = timezone.now() + datetime.timedelta(days=days)
  
  return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
  def test_no_questions(self):
    """질문 없으면 메시지 띄움"""
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available : 사용가능한 투표가 없습니다.")
    self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
  def test_past_question(self):
    ##발행일이 과거인 질문폼은 인덱스 페이지에 노출O
    question = create_question(question_text="Past question.", days=-30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(response.context["latest_question_list"], [question], )
    
  def test_future_question(self):
    ##발행일이 미래인 질문폼은 인덱스 페이지에 노출X
    create_question(question_text="Future question.", days= 30)     #미래 질문폼 생성
    response = self.client.get(reverse('polls:index'))
    self.assertContains(response, "No polls are available")
    self.assertQuerysetEqual(response.context["latest_question_list"], [] )


  def test_future_question_and_past_question(self):
      """
      Even if both past and future questions exist, only past questions
      are displayed.   미래 + 과거=> 과거 게시물만 노출
      """
      question = create_question(question_text="Past question.", days=-30) 
      create_question(question_text="Future question.", days=30)
      response = self.client.get(reverse('polls:index'))
      self.assertQuerysetEqual(
          response.context['latest_question_list'],
          [question],
      )

  def test_two_past_questions(self):
      """
      The questions index page may display multiple questions.      
      """ 
      question1 = create_question(question_text="Past question 1.", days=-30)
      question2 = create_question(question_text="Past question 2.", days=-5)
      response = self.client.get(reverse('polls:index'))
      self.assertQuerysetEqual(
          response.context['latest_question_list'],
          [question2, question1],
      )
  
class QuestionModelTests(TestCase): 
    
    def test_was_published_recently_with_future_question(self):    #미래 질문폼 확인
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)    #미래 시간대로 지정된 질문폼 생성(30일 뒤)      
        self.assertIs(future_question.was_published_recently(), False) # future_question.was_published_recently() != False면 메시지 띄움
  
    def test_was_published_recently_with_old_question(self):    #과거 질문폼 확인
      """
      was_published_recently() returns False for questions whose pub_date
      is older than 1 day.      
      """
      time = timezone.now() - datetime.timedelta(days=1, seconds=1)
      old_question = Question(pub_date=time)
      self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):   #최근 질문폼 확인(24 시간 이내)
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    ##3개의 테스트 실행된고 Assert ERROR 발생한 코드는 터미널에서 확인 가능