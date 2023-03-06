from django.core.validators import RegexValidator
from django.db import models


class Menu(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        validators=[
            RegexValidator(
                regex=r'^\w+$',
                message='URL содержит недопустимый символ'
            )
        ],
        verbose_name='URL'
    )

    class Meta:
        verbose_name = 'Элементы меню'
        verbose_name_plural = 'Элемент меню'

    def __str__(self):
        return self.title
