from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form =UserCreationForm()
    return render(request, 'index.html', {'form': form})
def Posts(request):
    posts = Post.objects.all()
    return render (request,'posts.html', {'posts':posts})
    