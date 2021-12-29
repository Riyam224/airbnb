from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, related_name="post_author" ,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    tags = TaggableManager()
    image = models.ImageField(upload_to="post/")
    created_at = models.DateField(default=timezone.now)
    description = models.TextField(max_length=2000)
    category = models.ForeignKey("Category", related_name="post_category" ,on_delete=models.CASCADE)
    slug = models.SlugField(blank=True , null=True)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)
       super(Post, self).save(*args, **kwargs) # Call the real save() method

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    


class Category(models.Model):
    name = models.CharField( max_length=200)

    
    def __str__(self):
        return self.name
