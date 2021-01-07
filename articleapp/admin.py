from django.contrib import admin
from articleapp.models import Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','writer','title','content','image']
    list_display_links = ['id','title']

