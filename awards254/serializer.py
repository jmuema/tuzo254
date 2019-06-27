from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title','description','image_path','owner','website_link']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','bio','myproject','profile_image','email']
