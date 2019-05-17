from django.db import models

# Create your models here.

from decimal import Decimal

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(verbose_name='Адрес', max_length=250)
    city = models.CharField(verbose_name='Город', max_length=100)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity