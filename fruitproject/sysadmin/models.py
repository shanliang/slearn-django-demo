from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=40)
	pub_date = models.DateTimeField('date published')
	article_id = models.IntegerField(default=0)
	summary = models.CharField(max_length=200)
	content = models.CharField(max_length=5000)
	author = models.CharField(max_length=30)


class Photo(models.Model):
	picture_id = models.IntegerField(default=0)
	#photo = models.ImageField(upload_to='/photos')	

