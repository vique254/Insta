from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    url('^$', views.index, name="index"),
    # url(r'^login/', views.login, name="login"),
    url(r'^home/', views.home, name="home"),
    url(r'^like/', views.like, name="like"),
    url(r'^dislike/', views.dislike, name="dislike"),
    url(r'^comment/<int:post_id>', views.comment, name="comment"),
    url(r'^profile/<str:username>', views.profile, name="profile"),
    # url(r'^register/', views.register, name="register"),
    # url(r'^loginuser/', views.login, name="validate"),
    url(r'^logout/', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^upload/', views.upload_photo, name="upload"),
    url(r'^search/', views.search, name="search"),
    url(r'^follow/<str:begin>/<str:end>', views.follow, name="follow"),
    url(r'^unfollow/<str:begin>/<str:end>', views.unfollow, name="unfollow"),
    path('signup/', views.SignUp.as_view(), name='signup'),
]