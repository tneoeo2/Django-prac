from django.contrib import admin
from .models import Question, Choice      #admin에서 제어할 권한을 부여




class QuestionAdmin(admin.ModelAdmin):
  #여러개의 필드가 있는 폼에서는 fieldset으로 분할하여 관리
  #fieldset [(fieldset 제목, )]
  fieldsets = [(None, {'fields':['question_text'], }),
               ('Date information', {'fields': ['pub_date']}), ]

admin.site.register(Question, QuestionAdmin)    #QuestionAdmin 두번째 인수로 전달 -> 발행일 설문 필드 앞으로 오게함
admin.site.register(Choice)






