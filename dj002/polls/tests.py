import datetime
from tarfile import PAX_NUMBER_FIELDS

from django.test import TestCase
from django.utils import timezone
# Create your tests here.

from .models import Question

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