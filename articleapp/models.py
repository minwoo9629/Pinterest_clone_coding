from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    project= models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='article/', null=True)
    created_at = models.DateField(auto_created=True, null=True)
