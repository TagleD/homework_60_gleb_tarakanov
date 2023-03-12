from django.db.models import Manager


class ProductManager(Manager):

    def all(self):
        return self.get_queryset().exclude(balance=0).exclude(is_deleted=True).order_by('category', 'name')


class BasketManager(Manager):
    def basket_total(self):
        products = self.get_queryset()
        total = 0
        for product in products:
            total += product.product_total()
        return total