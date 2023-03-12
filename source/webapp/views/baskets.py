from django.views.generic import View, ListView
from django.shortcuts import redirect, get_object_or_404
from webapp.forms import BasketForm
from webapp.models import Product, Basket



class BasketAddFormView(View):

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs.get('pk'))
        product_in_basket = Basket.objects.filter(product=product.pk)
        if product_in_basket:
            for product in product_in_basket:
                product.number += 1
                product.save()
            return redirect('products_view')
        else:
            basket_data = {
                'product': product,
                'number': 1
            }
            Basket.objects.create(**basket_data)
            return redirect('products_view')


class BasketProductsListView(ListView):
    template_name = 'baskets/basket_products_list.html'
    model = Basket
    context_object_name = 'basket'
    extra_context = {'basket_total': Basket.objects.basket_total()}
    ordering = ('added_at',)





# class BasketAddFormView(View):
#
#     def post(self, request, *args, **kwargs):
#         basket_form = BasketAddForm(data=request.POST)
#         if not basket_form.is_valid():
#             return redirect('products_view', basket_form=basket_form)
#         else:
#             product = get_object_or_404(Product, pk=kwargs.get('pk'))
#             basket = basket_form.save(commit=False)
#             basket.product = product
#             basket.save()
#             return redirect('products_view')





