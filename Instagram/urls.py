from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.timeline,name='Timeline'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^new/post$',views.new_post, name='newPost'),
    url(r'^new/location$',views.new_location, name='newLocation'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^edit/profile$',views.edit_profile, name='editProfile'),
    url(r'^people/',views.explore, name='people'),
    url(r'^like/$', views.like, name='like'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^userProfile/(\d+)',views.userprofile,name='userProfile'),
    url(r'^comment/$',views.comment,name='comment'),
    url(r'^changeProfile/(?P<username>\w{0,50})',views.change_profile,name='changeProfile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)