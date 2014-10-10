from django.contrib import admin
from register.models import Register

class RegisterAdmin(admin.ModelAdmin):
	list_display = ('nickname','email','password')

admin.site.register(Register, RegisterAdmin)


