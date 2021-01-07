from django.db import models
from django.contrib.auth.models import User
from articleapp.models import Article
# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now=True)