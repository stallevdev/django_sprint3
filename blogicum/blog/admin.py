"""Административная регистрация моделей: локации, категории и посты."""

from django.contrib import admin

from .models import Category, Location, Post

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)
