from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User, related_name="post_author" ,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    tags = TaggableManager()
    image = models.ImageField(upload_to="post/")
    created_at = models.DateField(default=timezone.now)
    description = models.TextField(max_length=2000)
    category = models.ForeignKey("Category", related_name="post_category" ,on_delete=models.CASCADE)
    


    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField( max_length=200)

    
    def __str__(self):
        return self.name
