from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, render, redirect
from sysadmin.models import Article
from .upload_form import UploadImageForm
from django.views.decorators.csrf import csrf_exempt
from .models import uploadPhoto
from .handle_uploaded_file import handle_uploaded_file


import MySQLdb

def index(request):
    latest_article_list = Article.objects.order_by('-id')[:30]
    for index, article in enumerate(latest_article_list):
        article.index = index + 1;
    template = loader.get_template('article/index.html')
    context = RequestContext(request, {
        'latest_article_list': latest_article_list,
    })
    return HttpResponse(template.render(context))

def addArticle(request):
    from django.db import connection
    article_id = request.GET['article-id']
    author = request.GET['author']
    title = request.GET['title']
    time = request.GET['time']
    summary = request.GET['summary']
    content = request.GET['content']
    db =  MySQLdb.connect(user='root', db='fruitdata', passwd='ssinsky')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO sysadmin_article (title, pub_date, article_id,summary,content,author) values (%s, %s, %s, %s, %s, %s)", [title, time, article_id,summary,content,author])
    db.close()
    return redirect('/sysadmin')

def delArticle(request):
    from django.db import connection
    delIds = request.GET['delete-ids']
    delIdsList = delIds.split(',')
    db =  MySQLdb.connect(user='root', db='fruitdata', passwd='ssinsky')
    cursor = connection.cursor()

    for delId in delIdsList:
        cursor.execute("DELETE FROM sysadmin_article WHERE  id = %s",delId)
    return redirect('/sysadmin')

def readArticle(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/article.html', {'article': article})  

@csrf_exempt
def uploadPhoto(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['photo'])
            return HttpResponse('ok')
    else:
        form = UploadImageForm()
    return render_to_response('photo/upload.html', {'form': form})

