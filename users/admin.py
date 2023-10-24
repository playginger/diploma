from django.contrib import admin

from .models import Post


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_Post = ('id', 'author', 'title', 'content')

