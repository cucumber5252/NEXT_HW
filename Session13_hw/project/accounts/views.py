from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile

# Create your views here.

def home(request):
    profiles = Profile.objects.all()
    return render(request, 'accounts/home.html', {'profiles': profiles})

def signup(request):
    if request.method == 'POST':
        exist_user = User.objects.filter(username = request.POST['username'])

        if exist_user:
            error = "이미 존재하는 아이디입니다."
            return render(request, 'accounts/signup.html', {"error": error})
        

        if request.POST['password1'] != request.POST['password2']:
            error = "비밀번호가 일치하지 않습니다."
            return render(request, 'accounts/signup.html', {"error": error})


        user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password1']
        )
        realname = request.POST['realname']
        nickname = request.POST['nickname']
        age = request.POST['age']

        profile = Profile(user = user, realname = realname, nickname = nickname, age = age)
        profile.save()

        auth.login(request, user)
        return redirect('blog:home')
        
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user, backend = "django.contrib.auth.backends.ModelBackend")
            return redirect('blog:home')
        
        error = '아이디 또는 비밀번호가 틀립니다'

        return render(request, 'accounts/login.html', {"error": error})

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('accounts:login')