from django.db import models

# Create your models here.


class Settings(models.Model):
    site_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="settings/")
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    description = models.TextField(max_length=1000)
    address =  models.CharField(max_length=200)
    fb_link = models.URLField( max_length=200)
    twitter_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)

    

    def __str__(self):
        return self.site_name

  