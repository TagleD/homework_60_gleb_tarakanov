from django.urls import path

from webapp.views.base import ProductsListView
from webapp.views.products import (
    ProductDetailView, ProductCreateView,
    ProductUpdateView, ProductDeleteView
)


urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('products', ProductsListView.as_view(), name='products_view'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add', ProductCreateView.as_view(), name='products_add'),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('article/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='confirm_delete')
    # path('categories/add', category_add_view, name='category_add'),
    # path('categories', categories_view, name='categories_view'),
    # path('categories/<int:pk>/delete', category_delete_view, name='category_delete'),
    # path('categories/<int:pk>/edit', category_edit_view, name='category_edit')
]
