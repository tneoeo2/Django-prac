import random
from django.shortcuts import render, HttpResponse


topics = [
  {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
  {'id': 2, 'title': 'view', 'body': 'View is ..'},
  {'id': 3, 'title': 'Model', 'body': 'Model is ..'},
]

def HTMLTemplate(articleTag):     #재사용가능한 템플릿으로 분리
  global topics
  ol = ''
  for topic in topics:
    ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'        
  return f'''
            <html>
            <body>
              <h1><a href ="/">Django</a></h1>                      
              <ul>
                {ol}
              </ul>
              {articleTag}
              <ul>
                <li><a href="/create/">create</a></li>
              </ul>
            </body>
            </html>
            '''

def index(request):     #request : 요청과 관련된 객체(이름 바꿔도 가능하나 관습적으로 request 사용)
  article = '''
    <h2>Welcome</h2>
    Hello, Django
    <p>This is article Tag.</p>
  '''
  return HttpResponse(HTMLTemplate(article))

  
def create(request):
  article = '''
  <form action="/create">
    <p><input type="text" name="title" placeholder="title..."></p>
    <p><textarea name="body" placeholder="body..."></textarea></p>
    <P><input type="submit"></p>
  </form>
  '''
  
  return HttpResponse(HTMLTemplate(article))
  
def read(request, id):
  global topics 
  article = ''
  for topic in topics: 
    if topic['id'] == int(id):    #선택한 id에 해당하는 페이지에 body 값 가져와 띄우기
      article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
  
  return HttpResponse(HTMLTemplate(article))

