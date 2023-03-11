from django.contrib import admin
from webapp.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'category', 'balance', 'coast')
    list_filter = ('id', 'name', 'description', 'image', 'category', 'balance', 'coast')
    search_fields = ('id', 'name', 'description', 'image', 'category', 'balance', 'coast')
    fields = ('id', 'name', 'description', 'image', 'category', 'balance', 'coast')
    readonly_fields = ('id', 'name', 'description', 'image', 'category', 'balance', 'coast')


admin.site.register(Product, ProductAdmin)
