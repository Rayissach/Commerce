from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(height_field=60, width_field=60, upload_to="static/auctions/images/")
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Categories, related_name="categories")
    
    def __str__(self):
        return f"{self.id}: {self.title} {self.image} {self.description} {self.price} {self.created} {self.categories}"

class Bids(models.Model):
    item = models.CharField(max_length=20)
    price = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_price")
    bidders = models.PositiveIntegerField()
    bid = models.DecimalField(max_digits=10, decimal_places=2)

class Comments(models.Model):
    pass
