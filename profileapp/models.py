from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from datetime import datetime

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/profile', ymd_path, uuid_name])
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name="프로필 이미지")
    filename = models.CharField(max_length=64, null=True, verbose_name="이미지 파일명")
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)