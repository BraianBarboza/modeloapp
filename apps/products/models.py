from django.db import models
from categories.models import Category

class Product(models.Model):
    name = models.CharField('nome', max_length=100)
    description = models.TextField('descrição', blank=True)
    fabrication_date = models.DateField('data de fabricação')
    is_active = models.BooleanField('ativo', default=True)
    price = models.DecimalField('preço', max_digits=10, decimal_places=2)
    photo = models.ImageField('foto', upload_to='products/photos/', blank=True)
    doc = models.FileField('documento', upload_to='products/docs/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='categoria')

    def __str__(self):
        return self.name