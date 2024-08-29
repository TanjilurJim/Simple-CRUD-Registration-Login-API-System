from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)

    description = models.CharField(max_length=600)

    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]) # Ensures price can't be negative
    


    def __str__(self):
        return f"{self.name},price ${self.price} "
    
