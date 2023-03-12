from django.urls import path

from webapp.views.base import ProductsListView
from webapp.views.baskets import BasketAddFormView, BasketProductsListView
from webapp.views.products import (
    ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView
)


urlpatterns = [
    #URL для отображения товаров
    path('', ProductsListView.as_view(), name='index'),
    path('products', ProductsListView.as_view(), name='products_view'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add', ProductCreateView.as_view(), name='products_add'),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('article/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='confirm_delete'),

    #URl для работы с корзиной
    path('basket/product/add/<int:pk>', BasketAddFormView.as_view(), name='basket_add_product'),
    path('basket/products/', BasketProductsListView.as_view(), name='basket_add_product'),
]
