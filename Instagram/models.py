from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from datetime import datetime
from django.conf import settings 
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    author  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image   = models.ImageField(default='default.png', blank=True)
    caption = models.TextField()
    likes   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.caption

class UserProfile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name =  models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    birth_date = models.DateField()
    password = models.CharField(max_length=150)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()    