"""Конфигурация приложения Django."""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Конфигурация приложения 'Ядро'."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Ядро'
