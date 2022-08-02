import datetime
from tarfile import PAX_NUMBER_FIELDS

from django.test import TestCase
from django.utils import timezone
# Create your tests here.

from .models import Question

class QuestionModelTests(TestCase):
  
  def test_was_published_recently_with_future_question(self):
      """
      was_published_recently() returns False for questions whose pub_date
      is in the future.
      """
      time = timezone.now() + datetime.timedelta(days=30)
      future_question = Question(pub_date=time)    #미래 시간대로 지정된 질문폼 생성(30일 뒤)      
      self.assertIs(future_question.was_published_recently(), False) # future_question.was_published_recently() != False면 메시지 띄움
 