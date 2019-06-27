from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

INTERGER_CHOICES= [tuple([x,x]) for x in renge(1,11)]

class UserRegistrationForm(UserCreationForm):
  email =forms.EmailField()

  class Meta: #gives us a nested space for configs and keeps them in 1 place
    model = User
    fields = ['username','email','password1','password2']

# class ProjectPostForm(forms.ModelForm):
#   class Meta:
#     model = Project
#     fields = ['title','description','image_path','website_link']

# class ReviewForm(forms.ModelForm):
#   class Meta:
#     models = Review
#     exclude = ['username','project']
#     widgets = {
#       'design': forms.Select(choices=INTEGER_CHOICES),
#       'usability': forms.Select(choices=INTEGER_CHOICES),
#       'content': forms.Select(choices=INTEGER_CHOICES),
#       'review': forms.TextInput(attrs={'placeholder':'Add a review'})
#     }