from ago import human
import pytz
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    image = models.ImageField(upload_to='home/')
    description = models.CharField(null=True, max_length=200)
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        result = datetime.now().replace(tzinfo=pytz.timezone('Africa/Nairobi')) - self.date
        return human(result)


class Follow(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_from')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to')

    def __str__(self):
        message = 'User {} follow {}'
        return message.format(self.user_from.user_django.username, self.user_to.user_django.username)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)