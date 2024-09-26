# blog/admin.py
from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'body')
    list_filter = ('tags',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'author', 'created_at')
    search_fields = ('body',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
