from django.contrib import messages
from django.views import View
from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404
from webapp.forms import BasketAddForm
from webapp.models import Product, Basket


class BasketAddFormView(FormView):
    form_class = BasketAddForm

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            number = form.cleaned_data.get('number')

            if not Basket.objects.filter(product=product).exists():
                # Проверяем остаток товаров на складе по введенному числу
                if number > product.balance:
                    messages.error(
                        request,
                        f'На складе всего {product.balance} товаров,'
                        f' поэтому добавление {number} невозможно'
                    )
                    return redirect('index')
                Basket.objects.create(product=product, number=number)
                messages.success(request, 'Желаемое количество товаров успешно добавлено!')
            else:
                basket = Basket.objects.filter(product=product).first()
                # Проверяем остаток товаров на складе по введенному числу + числу в корзине
                if (number + basket.number) > product.balance:
                    messages.error(
                        request,
                        f'Вы пытаетесь добавить {number + basket.number} с учетом {basket.number},'
                        f' которые уже добавили, а на складе всего {product.balance}'
                    )
                    return redirect('index')
                basket.number += number
                basket.save()
                messages.success(request, 'Желаемое количество товаров успешно добавлено!')
        return redirect('index')


class BasketDeleteOneView(View):
    def get(self, request, *args, **kwargs):
        basket_product = get_object_or_404(Basket, pk=kwargs.get('pk'))
        if not basket_product.number == 1:
            basket_product.number -= 1
            basket_product.save()
            messages.success(request, 'Количество товара в корзине уменьшено на 1')
        else:
            basket_product.delete()
            messages.success(request, 'Товар был удален из корзины, так как был в 1-ом числе')
        return redirect('basket_list')


class BasketDeleteView(View):

    def post(self, request, *args, **kwargs):
        basket_product = get_object_or_404(Basket, pk=kwargs.get('pk'))
        basket_product.delete()
        messages.success(request, 'Товар удален из корзины')
        return redirect('basket_list')
