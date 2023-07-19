from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(height_field=60, width_field=60)
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Categories, related_name="categories")
    # pass

class Bids(models.Model):
    item = models.CharField(max_length=20)
    price = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_price")
    bidders = models.PositiveIntegerField()
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    # pass

class Comments(models.Model):
    pass
