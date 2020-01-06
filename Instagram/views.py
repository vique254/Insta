from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome(request):
   
    return render (request, 'index.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register_form.html', {'form': form})