from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import (login as auth_login,  authenticate)
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse_lazy
# Models
from django.contrib.auth.models import User
from Instagram.models import *
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


# def index(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     return render(request, "index.html")


# def login(request):
#     _message = 'Please sign in'
#     if request.method == 'POST':
#         _username = request.POST['username']
#         _password = request.POST['password']
#         user = authenticate(username=_username, password=_password)
#         if user is not None:
#             if user.is_active:
#                 auth_login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#             else:
#                 _message = 'Your account is not activated'
#         else:
#             _message = 'Invalid login, please try again.'
#     context = {'message': _message}
#     return render(request, "registration/login.html",context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration_form.html'

@login_required(login_url='/accounts/login/')
def home(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    follow = Follow.objects.filter(user_from=my_user)
    complete_post = my_user.post_set.all()
    for f in follow:
        complete_post = complete_post | f.user_to.post_set.all()
    complete_post = complete_post.order_by('-date')

    all_users = User.objects.all()
    likes = Like.objects.filter(user=my_user)
    likes = [like.post.id for like in likes]

    context = dict(
        current_user=my_user,
        username=request.user.username,
        complete_post=complete_post,
        all_users=all_users,
        likes=likes
    )
    return render(request, "home.html", context)


def upload_photo(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        context = dict(username=request.user.username)
        return render(request, "upload.html", context)
    if request.method == 'POST':
        username = request.user.username
        
        last_post = Post.objects.filter(user=user).last()
        if last_post:
            photo_id = last_post.id + 1
        else:
            photo_id = 1
        description = request.POST['description']
        photo = request.FILES['file']
        photo_name = username + '_photo_' + str(photo_id)
        fs = FileSystemStorage()
        url_photo = fs.save(photo_name, photo)
        path_photo = fs.url(url_photo)

        post = Post.objects.create(photo=path_photo, description=description, user=user)
        return redirect('profile', username)


def profile(request, username):
    if not request.user.is_authenticated:
        return redirect('home')

    context = dict()
    if username == request.user.username:
        user = request.user
    else:
        user = User.objects.get(username=username)
        is_follow = Follow.objects.filter(user_from=request.user.post, user_to=user.post).exists()
        context.update(is_follow=is_follow)

    post = Post.objects.filter(user_id=user_id).order_by('-date')
    number_followers = Follow.objects.filter(user_to_id=user_id).count()
    number_victims = Follow.objects.filter(user_from_id=user_id).count()
    context.update(
        username=request.user.username,
        current_username=user.username,
        post=post,
        number_followers=number_followers,
        number_victims=number_victims,
        my_user=my_user
    )
    return render(request, "profile.html", context)


# def register(request):
#     if request.method == 'POST':
#         post_form_data = request.POST
#         data = dict(
#             username=post_form_data.get('username'),
#             email=post_form_data.get('email'),
#             first_name=post_form_data.get('name'),
#             password=post_form_data.get('password')
#         )
#         user = User.objects.create_user(**data)
#         return redirect('login')
#     return render('index')


# def validate_user(request):
#     return redirect('home')


def search(request):
    username = request.POST['search_username']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None
    if user:
        return redirect('profile', user.username)
    else:
        return redirect('profile', request.user.username)


def follow(request, begin, end):
    user_begin = User.objects.get(username=begin)
    user_end = User.objects.get(username=end)
    Follow.objects.create(user_from=user_begin.post, user_to=user_end.post)
    return redirect('profile', end)


def unfollow(request, begin, end):
    user_begin = User.objects.get(username=begin)
    user_end = User.objects.get(username=end)
    follow = Follow.objects.get(user_from=user_begin.post, user_to=user_end.post)
    follow.delete()
    return redirect('profile', end)


@csrf_exempt
def like(request):
    post_id = request.POST['post_id']
    post = Post.objects.get(id=post_id)
    
    data = dict(
        user=my_user,
        post=post
    )
    like = Like.objects.create(**data)

    response = dict(message='OK', likes_count=post.like_set.count())
    return JsonResponse(response)


@csrf_exempt
def dislike(request):
    post_id = request.POST['post_id']
    post = Post.objects.get(id=post_id)
    
    data = dict(
        user=my_user,
        post=post
    )
    like = Like.objects.get(**data)
    like.delete()
    response = dict(message='OK', likes_count=post.like_set.count())
    return JsonResponse(response)


def comment(request, post_id):
    
    comment = request.POST['comment']
    post = Post.objects.get(id=post_id)
    data = dict(
        content=comment,
        post=post,
        user=my_user
    )
    Comment.objects.create(**data)
    return redirect('home')