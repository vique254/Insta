from django.conf.urls import url
from . import views
from django

urlpatterns=[
    url(r'^$',views.signup,name='signup')
]