from django.contrib import admin

# Register your models here.
from .models import Comment, Like, Post

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)