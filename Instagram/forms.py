from django import forms
from .models import Post,Location,Profile,Comment

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields=['location']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username','post_date','likes','profilePhotos']


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }