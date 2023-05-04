from django.contrib import admin
from .models	import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['id','title','author','date']
    list_display_links = ['id','title']
    list_filter = ['date', 'author']
    search_fields = ['title',	'author']
    inlines = [
    CommentInline, 
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'content', 'author')