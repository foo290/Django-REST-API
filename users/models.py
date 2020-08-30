from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    img = models.ImageField(default='default_pfp.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    
    company = models.CharField(max_length=550, null=True, blank=True)
    github = models.CharField(max_length=550, null=True, blank=True)
    twitter = models.CharField(max_length=550, null=True, blank=True)
    instagram = models.CharField(max_length=550, null=True, blank=True)
    
    website = models.CharField(max_length=550, null=True, blank=True)


    def __str__(self):
        return str(self.user.username)