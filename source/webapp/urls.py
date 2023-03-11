from django.urls import path



from webapp.views.products import (
    products_view, product_view, products_add_view,
    products_edit_view, products_delete_view,
    confirm_delete
)


urlpatterns = [
    path('', products_view, name='index'),
    path('products', products_view, name='products_view'),
    path('products/<int:pk>', product_view, name='product_detail'),
    path('products/add', products_add_view, name='products_add'),
    path('products/<int:pk>/delete', products_delete_view, name='product_delete'),
    path('products/<int:pk>/edit', products_edit_view, name='product_edit'),
    path('article/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete')
    # path('categories/add', category_add_view, name='category_add'),
    # path('categories', categories_view, name='categories_view'),
    # path('categories/<int:pk>/delete', category_delete_view, name='category_delete'),
    # path('categories/<int:pk>/edit', category_edit_view, name='category_edit')
]
