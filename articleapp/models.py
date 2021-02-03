import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project
from uuid import uuid4
from datetime import datetime

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/article', ymd_path, uuid_name])

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    project= models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name="첨부파일")
    filename = models.CharField(max_length=64, null=True, verbose_name="첨부파일명")
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through='Like')

    class Meta:
        ordering = ['created_at']
    
    @property
    def like_count(self):
        return self.like_user_set.count()
        
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Article, self).delete(*args, **kwargs)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user','article')