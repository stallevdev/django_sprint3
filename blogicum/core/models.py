from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель, содержащая флаг публикации и дату создания."""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        """Мета."""

        abstract = True
