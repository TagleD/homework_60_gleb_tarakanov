from django.db import models



class Basket(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        related_name='basked',
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    number = models.PositiveIntegerField(
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

    # objects = BasketManager()

    def __str__(self):
        return f'в корзине {self.number} товаров'

    def product_total(self):
        total = self.product.coast * self.number
        return total

    def product_name(self):
        name = self.product.name
        return name
