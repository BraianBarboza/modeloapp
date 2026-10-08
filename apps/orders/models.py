from django.db import models
from customers.models import Client
from products.models import Product

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('CASH', 'Dinheiro'),
        ('CARD', 'Cartão'),
        ('PIX', 'Pix'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('PAID', 'Pago'),
        ('CANCELED', 'Cancelado'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField('pagamento', max_length=10, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='cliente')

    def __str__(self):
        return f'Pedido #{self.pk} - {self.client}'

    def update_total(self):
        self.total = sum(item.subtotal for item in self.items.all())
        self.save(update_fields=['total'])


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField('quantidade', default=1)
    unit_price = models.DecimalField('preço unitário', max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='produto')
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)