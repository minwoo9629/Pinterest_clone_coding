from django.contrib import admin
from commentapp.models import Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'writer','content','created']
    list_display_links = ['id', 'content']