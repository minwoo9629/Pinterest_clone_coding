from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='article/', null=True)
    created_at = models.DateField(auto_created=True, null=True)
