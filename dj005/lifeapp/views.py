import random
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
  {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
  {'id': 2, 'title': 'view', 'body': 'View is ..'},
  {'id': 3, 'title': 'Model', 'body': 'Model is ..'},
]

def HTMLTemplate(articleTag, id=None):     #재사용가능한 템플릿으로 분리
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
                <li>
                  <form action="/delete/" method="post">
                  <input type="hidden" name="id" value="{id}"/>
                   <input type="submit" value="delete" />
                  </form>
                </li>
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
  
def read(request, id):
  global topics 
  article = ''
  for topic in topics: 
    if topic['id'] == int(id):    #선택한 id에 해당하는 페이지에 body 값 가져와 띄우기
      article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
  
  return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
  global nextId
  print("request.method = ", request.method)   ## get방식 post방식인지 확인
  if request.method == 'GET':
    article = '''
    <form action="/create/" method="post" >
      <p><input type="text" name="title" placeholder="title..."></p>
      <p><textarea name="body" placeholder="body..."></textarea></p>
      <P><input type="submit"></p>
    </form>
    '''
    return HttpResponse(HTMLTemplate(article))
  elif request.method == 'POST':
    print(request.POST['title'])
    title = request.POST['title']
    body = request.POST['body']
    newTopic = {"id": nextId, "title": title, "body": body}
    topics.append(newTopic)
    url = '/read/'+ str(nextId)
    nextId = nextId + 1
    return redirect(url)      #생성된 페이지 url로 이동

@csrf_exempt
def delete(request):
  global topics
  
  if request.method == 'POST':
    id = request.POST['id']
    newTopics = []
    for topic in topics:
      if topic['id'] != int(id):
          newTopics.append(topic)
    topics = newTopics
    return redirect('/')