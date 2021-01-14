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
    like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through='Like')

    class Meta:
        ordering = ['-created_at']
    
    @property
    def like_count(self):
        return self.like_user_set.count()
        
    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user','article')