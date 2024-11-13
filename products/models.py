from django.db import models
from providers.models import Providers

class Product(models.Model):
    categories = (
        ('food', 'Food'),
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('furniture', 'Furniture'),
        ('appliances', 'Appliances'),
        ('books', 'Books'),
        ('toys', 'Toys'),
        ('other', 'Other')
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=12, choices=categories)
    provider = models.ForeignKey(Providers, on_delete=models.PROTECT)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

