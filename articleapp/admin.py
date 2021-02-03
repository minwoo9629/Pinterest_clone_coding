from django.contrib import admin
from articleapp.models import Article, Like
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','writer','title','content','image', 'like_count', 'created_at', 'updated_at']
    list_display_links = ['id','title']
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user','article']

