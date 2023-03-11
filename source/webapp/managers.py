from django.db.models import Manager


class ProductManager(Manager):

    def all(self):
        return self.get_queryset().exclude(balance=0).exclude(is_deleted=True).order_by('category', 'name')