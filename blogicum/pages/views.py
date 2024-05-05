"""Представления (views) для обработки запросов приложения."""

from django.shortcuts import render


def about(request):
    """Отображает страницу 'О сайте'."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Отображает страницу с правилами использования сайта."""
    template = 'pages/rules.html'
    return render(request, template)
