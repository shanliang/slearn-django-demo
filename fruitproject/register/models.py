from django.db import models

# Create your models here.
class Register(models.Model):
	nickname = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=30)

	def __unicode__(self):
		return "%s, %s, %s" % (self.nickname, self.email, self.password)
