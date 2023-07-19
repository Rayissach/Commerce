from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=20)
    # description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    # pass

class Categories(models.Model):
    categories = models.CharField(max_length=15)
    # list_item = models.ManyToManyField(Listing, blank=True, related_name="categories")

class Bids(models.Model):
    item = models.CharField(max_length=20)
    price = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_price")
    # bidders = models.PositiveIntegerField()
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    # pass

class Comments(models.Model):
    pass
