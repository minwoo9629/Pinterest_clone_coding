from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=255, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    created = models.DateTimeField(auto_now=True)