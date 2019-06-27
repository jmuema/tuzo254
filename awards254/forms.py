from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,11)]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:     #gives us a nested name space for configs and keeps them in 1 place
        model = User
        fields = ['username','email','password1','password2']

class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','image_path','website_link']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['username','project']
        widgets = {
            'design': forms.Select(choices=INTEGER_CHOICES),
            'usability': forms.Select(choices=INTEGER_CHOICES),
            'content': forms.Select(choices=INTEGER_CHOICES),
            'review': forms.TextInput(attrs={'placeholder':'Add a review'})
        }