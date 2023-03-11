from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product

from webapp.forms import ProductForm
from webapp.models import CategoryChoice


def products_view(request):
    products = Product.objects.exclude(balance=0).order_by(
        'category', 'name'
    )
    context = {'products': products}
    return render(request, 'products.html', context=context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)


def products_add_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_add.html', context={
            'choices': CategoryChoice.choices,
            'form': form
        })

    form = ProductForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request, 'product_add.html', context={
            'choices': CategoryChoice.choices,
            'form': form
        })
    else:
        product = Product.objects.create(**form.cleaned_data)
        return redirect('product_detail', pk=product.pk)





# def products_delete_view(request, pk):
#     product = Product.objects.get(pk=pk)
#     product.delete()
#     return redirect('products_view')


def products_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
        context = {'form': form, 'product': product}
        return render(request, 'product_edit.html', context=context)

    form = ProductForm(instance=product)
    context = {'form': form, 'product': product}
    return render(request, 'product_edit.html', context=context)


def products_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')