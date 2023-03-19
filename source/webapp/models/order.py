from django.core.validators import RegexValidator
from django.db import models

phone_regex_KZ = RegexValidator(
    regex=r'^7\d{9}$',
    message="Номер телефона должен быть из 10 цифр, начиная с '7'."
)


class Order(models.Model):
    username = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Имя пользователя'
    )
    phone = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[phone_regex_KZ],
        verbose_name='Телефонный номер'
    )
    address = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='Адрес'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )

    def __str__(self):
        return f'Заказчик -{self.username}, адресс - {self.address}'
