from django.db import models
from uuid import uuid4
from datetime import datetime

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/project', ymd_path, uuid_name])
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=255, null=True)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=True, verbose_name="프로젝트 썸네일")
    filename = models.CharField(max_length=64, null=True, verbose_name="이미지 파일명")
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title