from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
   title = models.CharField(max_length=200)
   content = models.TextField()
   category = models.TextField()
   date = models.DateTimeField(auto_now_add=True)

   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', default='')

   def __str__(self):
      return self.title
   
class Comment(models.Model):
   article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'comments')
   content = models.TextField()

   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', default='')

   def __str__(self):
      return self.content


class Recomment(models.Model):
   comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name = 'recomments')
   content = models.TextField()

   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recomments', default='')

   def __str__(self):
      return self.content