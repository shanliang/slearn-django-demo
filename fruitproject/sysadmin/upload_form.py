#In upload_forms.py...
from django import forms

class UploadImageForm(forms.Form):
   picture_id = forms.CharField(max_length=50)
   photo = forms.FileField()