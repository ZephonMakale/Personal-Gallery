from django.contrib import admin

from .models import Author, Category, Post, PostView

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostView)
