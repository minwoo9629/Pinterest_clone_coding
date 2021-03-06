# Generated by Django 3.1.4 on 2021-02-02 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='filename',
            field=models.CharField(max_length=64, null=True, verbose_name='이미지 파일명'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='project/', verbose_name='프로젝트 썸네일'),
        ),
    ]
