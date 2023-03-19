from django.db import models


class OrderProduct(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        related_name='order_product',
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    order = models.ForeignKey(
        'webapp.Order',
        related_name='order',
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    number = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='Количество',
        default=1
    )
