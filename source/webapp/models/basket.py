from django.db import models

class Basket(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        related_name='basked',
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    number = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Количество',
        default=1
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Время редактирования"
    )
