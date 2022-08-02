from django.contrib import admin
from .models import Question, Choice      #admin에서 제어할 권한을 부여

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3         #기본으로 3가지 선택 항목 제공

class QuestionAdmin(admin.ModelAdmin):
  #여러개의 필드가 있는 폼에서는 fieldset으로 분할하여 관리
  #fieldset [(fieldset 제목, )]
  fieldsets = [(None, {'fields':['question_text'], }),  
               ('Date information', {'fields': ['pub_date'], 
                'classes' : ['collapse']}),     #
               ]
  
  inlines = [ChoiceInline]    #Choice 객체는 Question 관리자 페이지에서 편집됨
    
  list_display = ('question_text', 'pub_date', 'was_published_recently')   #list보기에서 표시할 항목 설정
  list_filter = ['pub_date']   #사이드바에 필터링 추가
  search_fields = ['question_text']      # 검색 기능 추가: 변경 목록 위에 검색 창 추가(LIKE 쿼리 사용)
  
  

admin.site.register(Question, QuestionAdmin)    #QuestionAdmin 두번째 인수로 전달 -> 발행일 설문 필드 앞으로 오게함






