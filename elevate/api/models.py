from django.db import models
from django.core.validators import MinValueValidator

#importing the packages

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token





# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)

    description = models.CharField(max_length=600)

    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]) # Ensures price can't be negative
    


    def __str__(self):
        return f"{self.name},price ${self.price} "
    

@receiver(post_save, sender=User) 
def generate_auth_token(sender,instance=None, created = False, **kwargs):

    if created:

        Token.objects.create(user=instance)


