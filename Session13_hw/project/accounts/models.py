from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    realname = models.TextField(max_length=10, default = '')
    nickname = models.TextField(max_length=10, default = '')
    age	= models.PositiveIntegerField(help_text="User Age", blank=True, null=True)