

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from webapp.forms import OrderForm
from webapp.models import Basket, Order, OrderProduct


class OrderAddView(View):

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            order = Order.objects.create(username=username, phone=phone, address=address)
            basket_products = Basket.objects.all()

            for basket_product in basket_products:
                OrderProduct.objects.create(product=basket_product.product, order=order, number=basket_product.number)
                basket_product.product.balance -= basket_product.number
                basket_product.product.save()
            basket_products.delete()
            messages.success(request, 'Ваш заказ успешно создан')
            return redirect('index')
        else:
            reverse('basket_list', kwargs={'form': form})

