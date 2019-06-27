# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Models):
  title = models.CharField(max_length = 50)
  description = models.CharField(max_length =100)
  image_path = models.ImageField(Upload_to='project_images/')
  owner = models.ForeignKey(User,on_delete=models.CASCADE)
  website_link = models.CharField(max_length =100)
  
  @classmethod
  def search_by_title(cls,title):
    searched= cls.objects.filter(title_icontains=title)
    return searched

  def __str__(self):
    return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    #one user has one profile
    bio= models.CharField(max_length =100, default="Digital eye candy")
    myproject = models.ForeignKey(Project)
    profile_image= models.ImageField(default='default.jpeg')
    email= models.CharField(max_length =50)

    def __str__(self):
        return f"{self.user.username}'s Profile"
        