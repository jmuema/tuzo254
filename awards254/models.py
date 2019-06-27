from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length =50)
    description = models.CharField(max_length =100)
    image_path = models.ImageField(upload_to='project_images/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    website_link= models.CharField(max_length =100)
    
    @classmethod
    def search_by_title(cls,title):
        searched= cls.objects.filter(title__icontains=title)
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

class Review(models.Model):
    username= models.ForeignKey(User)
    design= models.CharField(max_length=2)
    usability= models.CharField(max_length=2)
    content= models.CharField(max_length=2)
    review = models.TextField(max_length=100,null=True)
    project = models.ForeignKey(Project)
    


