from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# 文章模型
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# 用户模型
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)