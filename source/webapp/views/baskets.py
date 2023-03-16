from django.views.generic import View, ListView, FormView
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
                Basket.objects.create(product=product, number=number)
            else:
                basket = Basket.objects.filter(product=product).first()
                basket.number += number
                basket.save()
        return redirect('index')


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
