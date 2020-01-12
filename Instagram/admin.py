from django.contrib import admin
from .models import MyUser,Follow,Post,Comment,Like
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)