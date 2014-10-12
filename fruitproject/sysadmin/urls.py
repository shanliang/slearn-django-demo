from django.conf.urls import patterns, url

from sysadmin  import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^addArticle/$', views.addArticle, name='addArticle'),
    url(r'^deleteArticle/$', views.delArticle, name='delArticle'),
    url(r'^uploadPhoto/$', views.uploadPhoto, name='uploadPhoto'),
    url(r'^(\d+)/$', views.readArticle, name='readArticle'),
)