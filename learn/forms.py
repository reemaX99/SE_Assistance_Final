from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import learn




class LearnForm(forms.ModelForm):
    class Meta:
        model = learn
        fields= ['title','description','urlLearn','category','diffcality_type','semester_type',
                 'image','videofile','tags']


