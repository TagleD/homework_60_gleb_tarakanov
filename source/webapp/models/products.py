from django.db import models
from django.db.models import TextChoices
from django.core.validators import MinValueValidator
from django.utils import timezone
from webapp.managers import ProductManager


class CategoryChoice(TextChoices):
    OTHER = 'OTHER', 'Другое'
    RIFLES = 'RIFLES', 'Винтовки'
    MELEE = 'MELEE', 'Ближнее'
    PISTOLS = 'PISTOLS', 'Пистолеты'
    SNIPERS = 'SNIPERS', 'Снайперские'


# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Наименование'
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=False,
        verbose_name="Описание"
    )
    image = models.CharField(
        max_length=3000,
        verbose_name="URL картинки"
    )
    category = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Категория',
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER
    )
    balance = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Остаток',
        validators=[MinValueValidator(1)],
        default=0
    )
    coast = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        verbose_name='Стоимость'
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время добавления"
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None
    )

    objects = ProductManager()

    def __str__(self):
        return f'{self.name} - {self.added_at}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
