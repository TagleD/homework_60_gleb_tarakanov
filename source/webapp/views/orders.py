from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from webapp.forms import OrderForm
from webapp.models import Basket, Order, OrderProduct, Product


class OrderCreateView(SuccessMessageMixin, CreateView):
    template_name = 'baskets/basket_products_list.html'
    model = Order
    form_class = OrderForm
    success_message = 'Заказ успешно создан!'
    success_url = reverse_lazy('index')

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
        context['basket'] = Basket.objects.all()
        return context

    def form_valid(self, form):
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
        return redirect('index')
