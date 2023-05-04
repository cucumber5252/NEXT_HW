from django.shortcuts import render, redirect
from .models import Post, Comment

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


@login_required(login_url='/accounts/login/')
def new(request):

    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            cost = request.POST['cost'],
            author = request.user
        )
        return redirect('blog:detail', new_post.pk)
    
    return render(request, 'blog/new.html')
    

@login_required(login_url='/accounts/login/')
def detail(request, post_pk):

    post = Post.objects.get(id = post_pk)
    
    if request.method == "POST":
        Comment.objects.create(
            post = post,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('blog:detail', post_pk)
    
    return render(request, 'blog/detail.html', {'post': post})


@login_required(login_url='/accounts/login/')
def update(request, post_pk):

    post = Post.objects.get(id = post_pk)

    if request.method == "POST":
        post_to_update = Post.objects.filter(id = post_pk)
        post_to_update.update(
            title = request.POST['title'],
            content = request.POST['content'],
            cost = request.POST['cost']
        )
        return redirect('blog:detail', post_pk)
    
    return render(request, 'blog/update.html', {'post': post})


@login_required(login_url='/accounts/login/')
def delete(request, post_pk):

    post = Post.objects.get(id = post_pk)
    post.delete()

    return redirect('blog:home')


@login_required(login_url='/accounts/login/')
def deleteComment(request, post_pk, comment_id):
   Comment.objects.get(id = comment_id).delete()
   return redirect('blog:detail', post_pk)



