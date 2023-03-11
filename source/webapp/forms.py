from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'balance', 'coast')
        labels = {
            'name': 'Наименование продукта',
            'description': 'Описание продукта',
            'image': 'URL картинки',
            'category': 'Выберите категорию из списка',
            'balance': 'Введите остаток товара',
            'coast': 'Цена товара'
        }
