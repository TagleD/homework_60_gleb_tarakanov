from django import forms
from webapp.models import Product, Order


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


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


class BasketAddForm(forms.Form):
    number = forms.IntegerField(min_value=1, required=True, label='Количество')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('username', 'phone', 'address')
        labels = {
            'username': 'Введите свое имя',
            'phone': 'Введите ваш телефон',
            'address': 'Введите ваш адрес'
        }
