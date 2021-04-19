from django.db import models

from shop.models import Product
# Create your models here.


class Order (models.Model):
    first_name = models.CharField("Имя", max_length=60)
    last_name = models.CharField("Фамилия", max_length=60)
    phone_number = models.CharField("Номер телефона", max_length=13, null=True)
    email = models.EmailField("Электронная почта", null=True, blank=True)
    address = models.CharField("Адрес", max_length=150)
    postal_code = models.CharField("Электронная почта", max_length=30)
    city = models.CharField("Город", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField("Оплачено", default=False)  # оплачен ли заказ

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        # общая сумма заказа
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

