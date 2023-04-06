from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
   if request.method == "POST":

      print(request.POST)

      new_article = Article.objects.create(
         title = request.POST['title'],
         content = request.POST['content'],
         category = request.POST['category'],
      )
      return redirect('list')

   return render(request, 'new.html')


def list(request):
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
   return render(request, 'list.html', {'articles': articles, 'hobby_count': hobby_count, 'food_count': food_count, 'programming_count': programming_count})


def detail(request, article_id):
   articles = Article.objects.get(id = article_id)
   
   return render(request, 'detail.html', {'article': articles})


def category(request, article_category):

   hobby_articles = Article.objects.filter(category = "hobby")
   food_articles = Article.objects.filter(category = "food")
   programming_articles = Article.objects.filter(category = "programming")

   if article_category == 'hobby':
      return render(request,'hobby.html', {'articles': hobby_articles})
   elif article_category == 'food':
      return render(request,'food.html', {'articles': food_articles})
   elif article_category == 'programming':
      return render(request,'programming.html', {'articles': programming_articles})