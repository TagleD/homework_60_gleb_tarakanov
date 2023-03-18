from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm, BasketAddForm


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket_add_form'] = BasketAddForm()
        context.update(kwargs)
        return super().get_context_data(**context)


class ProductCreateView(SuccessMessageMixin, CreateView):
    template_name = 'products/product_add.html'
    model = Product
    form_class = ProductForm
    success_message = 'Товар успешно добавлен!'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'products/product_edit.html'
    model = Product
    form_class = ProductForm
    success_message = 'Товар успешно изменен!'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'products/product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    success_message = 'Товар успешно удален!'
