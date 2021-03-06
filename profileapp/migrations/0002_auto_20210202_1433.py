# Generated by Django 3.1.4 on 2021-02-02 05:33

from django.db import migrations, models
import profileapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='filename',
            field=models.CharField(max_length=64, null=True, verbose_name='이미지 파일명'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profileapp.models.get_file_path, verbose_name='프로필 이미지'),
        ),
    ]
