from .models import Post,Follow,Comment,Like
from django.forms import ModelForm
from django import forms
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image','description','date','user']
        


class FollowForm(ModelForm):
    class Meta:
        model = Follow
        fields = ['user_from','user_to']
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content','date','user','post']
        
class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ['user','post']                