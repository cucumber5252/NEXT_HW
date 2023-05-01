from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Article, Comment, Recomment

# Create your views here.

def signup(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      exist_user = User.objects.filter(username = username)

      if exist_user:
         error = "이미 존재하는 유저입니다."
         return render(request, 'registration/signup.html', {"error": error})

      new_user = User.objects.create_user(username=username, password=password)
      
      auth.login(request, new_user)
      
      return redirect('login')
   
   return render(request, 'registration/signup.html')


def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username, password=password)

      if user is not None:
         auth.login(request, user, backend = "django.contrib.auth.backends.ModelBackend")
         return redirect('home')
      error = '아이디 또는 비밀번호가 틀립니다'

      return render(request, 'registration/login.html', {"error": error})

   return render(request, 'registration/login.html')


def logout(request):
   auth.logout(request)
   return redirect('home')


@login_required(login_url='/registration/login/')
def home(request):
   articles = Article.objects.all()
   hobby_count = 0
   food_count = 0
   programming_count = 0
   for article in articles:
      if article.category == "hobby":
         hobby_count +=1
      elif article.category == "food":
         food_count +=1
      elif article.category == "programming":
         programming_count +=1
   return render(request, 'home.html', {'articles': articles, 'hobby_count': hobby_count, 'food_count': food_count, 'programming_count': programming_count})


@login_required(login_url='/registration/login/')
def create(request):
   if request.method == "POST":
      new_article = Article.objects.create(
         title = request.POST['title'],
         content = request.POST['content'],
         category = request.POST['category'],
         author = request.user
      )
      return redirect('home')

   return render(request, 'create.html')


@login_required(login_url='/registration/login/')
def update(request, article_id):
   article = Article.objects.get(id=article_id)

   if request.method =='POST':
      Article.objects.filter(id=article_id).update(
         title = request.POST['title'],
         content = request.POST['content'],
         category = request.POST['category'],
         author = request.user
      )
      return redirect('detail', article_id)
   return render(request, 'update.html', {'article': article})


@login_required(login_url='/registration/login/')
def category(request, category_name):
   articles = Article.objects.filter(category = category_name)
   return render(request, 'category.html', {'articles': articles})


@login_required(login_url='/registration/login/')
def delete(request, article_id):
   article = Article.objects.get(id=article_id)
   article.delete()
   return redirect('home')


@login_required(login_url='/registration/login/')
def detail(request, article_id):
   article = Article.objects.get(id = article_id)
   
   if request.method == "POST":
      Comment.objects.create(
         article = article,
         content = request.POST['content'],
         author = request.user
      )
      return redirect('detail', article_id)
   
   return render(request, 'detail.html', {'article': article})


@login_required(login_url='/registration/login/')
def deleteComment(request, article_id, comment_id):
   Comment.objects.get(id = comment_id).delete()
   return redirect('detail', article_id)


@login_required(login_url='/registration/login/')
def recomment(request, article_id, comment_id):
   article = Article.objects.get(id = article_id)
   comment = Comment.objects.get(id = comment_id)
   
   other_comments = Comment.objects.filter(article__id = article_id).exclude(id = comment_id)

   if request.method == "POST":
      Recomment.objects.create(
         comment = comment,
         content = request.POST['content'],
         author = request.user
      )
      return redirect('recomment', article_id, comment_id)
   
   return render(request, 'recomment.html', {'article': article, 'comment': comment, 'other_comments': other_comments})

@login_required(login_url='/registration/login/')
def deleteRecomment(request, article_id, comment_id, recomment_id):
   Recomment.objects.get(id = recomment_id).delete()
   return redirect('recomment', article_id, comment_id)