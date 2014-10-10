from django.conf.urls import patterns, url

from register  import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.list, name='list'),
    url(r'^addUser/$', views.addUser, name='addUser'),

)