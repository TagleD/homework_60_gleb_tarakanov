from django.views import View
from django.views.generic import ListView, FormView
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
                    return redirect('index')
                Basket.objects.create(product=product, number=number)
            else:
                basket = Basket.objects.filter(product=product).first()
                # Проверяем остаток товаров на складе по введенному числу + числу в корзине
                if (number + basket.number) > product.balance:
                    return redirect('index')
                basket.number += number
                basket.save()
        return redirect('index')


class BasketDeleteOneView(View):
    def get(self, request, *args, **kwargs):
        basket_product = get_object_or_404(Basket, pk=kwargs.get('pk'))
        if not basket_product.number == 1:
            basket_product.number -= 1
            basket_product.save()
        else:
            basket_product.delete()
        return redirect('basket_list')


class BasketDeleteView(View):

    def post(self, request, *args, **kwargs):
        basket_product = get_object_or_404(Basket, pk=kwargs.get('pk'))
        basket_product.delete()
        return redirect('basket_list')





class BasketProductsListView(ListView):
    template_name = 'baskets/basket_products_list.html'
    model = Basket
    context_object_name = 'basket'
    ordering = ('added_at',)

    def get_count(self):
        total = 0
        baskets = Basket.objects.all()
        for basket in baskets:
            product = get_object_or_404(Product, pk=basket.product_id)
            total += basket.number * product.coast
        return total

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['basket_total'] = self.get_count()
        return context
