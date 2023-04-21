from django.shortcuts import render, redirect
from .models import Article, Comment, Recomment

# Create your views here.


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


def create(request):
   if request.method == "POST":
      new_article = Article.objects.create(
         title = request.POST['title'],
         content = request.POST['content'],
         category = request.POST['category'],
      )
      return redirect('home')

   return render(request, 'create.html')

def update(request, article_id):
   article = Article.objects.get(id=article_id)

   if request.method =='POST':
      Article.objects.filter(id=article_id).update(
         title = request.POST['title'],
         content = request.POST['content'],
         category = request.POST['category'],
      )
      return redirect('detail', article_id)
   return render(request, 'update.html', {'article': article})


def category(request, category_name):
   articles = Article.objects.filter(category = category_name)
   return render(request, 'category.html', {'articles': articles})


def delete(request, article_id):
   article = Article.objects.get(id=article_id)
   article.delete()
   return redirect('home')



def detail(request, article_id):
   article = Article.objects.get(id = article_id)
   
   if request.method == "POST":
      Comment.objects.create(
         article = article,
         content = request.POST['content']
      )
      return redirect('detail', article_id)
   
   return render(request, 'detail.html', {'article': article})



def deleteComment(request, article_id, comment_id):
   Comment.objects.get(id = comment_id).delete()
   return redirect('detail', article_id)




def recomment(request, article_id, comment_id):
   article = Article.objects.get(id = article_id)
   comment = Comment.objects.get(id = comment_id)
   
   other_comments = Comment.objects.filter(article__id = article_id).exclude(id = comment_id)

   if request.method == "POST":
      Recomment.objects.create(
         comment = comment,
         content = request.POST['content']
      )
      return redirect('recomment', article_id, comment_id)
   
   return render(request, 'recomment.html', {'article': article, 'comment': comment, 'other_comments': other_comments})


def deleteRecomment(request, article_id, comment_id, recomment_id):
   Recomment.objects.get(id = recomment_id).delete()
   return redirect('recomment', article_id, comment_id)