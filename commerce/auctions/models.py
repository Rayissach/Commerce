from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    pass

class Bids(models.Model):
    item = models.CharField()
    price = models.ForeignKey()
    bidders = models.ForeignKey()
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    
    pass

class Comments(models.Model):
    pass