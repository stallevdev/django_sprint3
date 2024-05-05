"""Представления (views) для обработки запросов приложения."""

from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def get_posts(post_objects):
    """Посты, опубликованные и с опубликованной категорией"""
    return post_objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    """Главная страница с перечнем публикаций."""
    template = 'blog/index.html'
    post_list = get_posts(Post.objects).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Отображает подробную информацию о конкретной публикации."""
    template = 'blog/detail.html'
    posts = get_object_or_404(get_posts(Post.objects), id=post_id)
    context = {'post': posts}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Отображает публикации, принадлежащие определённой категории."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = get_posts(category.posts)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
