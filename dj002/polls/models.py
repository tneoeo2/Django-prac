import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

##다-대-일(many-to-one), 다-대-다(many-to-many), 일-대-일(one-to-one) 과 같은 모든 일반 데이터베이스의 관계들를 지원
class Question(models.Model):
  question_text = models.CharField(max_length=200)    #question_text, pub_data : 데이터베이스 필드 이름(컬럼명)
  pub_date = models.DateTimeField('data publised')

  ##display() decorator 사용 
  @admin.display(boolean=True, ordering='pub_date', description='Published recently?')   
  def was_published_recently(self):
    now = timezone.now()
    #최근 발행일은 어제가 아니고 미래도 아니게끔 수정
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
      
    # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  
  def __str__(self):
    return self.question_text
  
class Choice(models.Model):   
  ##Question -- Choice: 1:N 관계 : N인 쪽에서 관계 선언(대상이 되는 클래스, 삭제시 이슈에 대한 설정)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)      #ForeignKey :  Choice가 하나의 question에 관계한다는것을 알려줌
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)    #설문자 수

  def __str__(self):
    return self.choice_text

  
  