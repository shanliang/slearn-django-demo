from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from register.models import Register

import MySQLdb

# "-id" : Descending id order
def index(request):
    return render_to_response('register/index.html')
    

def list(request):
    latest_register_list = Register.objects.order_by('-id')[:25]
    template = loader.get_template('register/list.html')
    context = RequestContext(request, {
        'latest_register_list': latest_register_list,
    })
    return HttpResponse(template.render(context))


def addUser(request):
	from django.db import connection
	name = request.GET['nickname']
	email = 'test@email.com'
	pwd = request.GET['password']
	db =  MySQLdb.connect(user='root', db='fruitdata', passwd='ssinsky')
	cursor = connection.cursor()
	cursor.execute("INSERT INTO register_register (nickname, email, password) values (%s, %s, %s)", [name, email, pwd])
	db.close()


	info = '<h2>SUCCESS! You have added:</h2>' + '<br>' + name + '<br>' + email + '<br>' + pwd

	return HttpResponse(info)



