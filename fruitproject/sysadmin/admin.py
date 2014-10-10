from django.contrib import admin
from sysadmin.models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('article_id','title','pub_date','summary','content')

admin.site.register(Article, ArticleAdmin)


