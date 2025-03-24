from django.db import models


# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    description = models.TextField()
    net_worth = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.name  # damit in DB/View anzeigen lassen


class Seller(models.Model):
    name = models.CharField(max_length=225)
    contact_info = models.TextField()
    markets = models.ManyToManyField(Market, related_name="sellers")

    def __str__(self):
        return self.name  # damit in DB/View anzeigen lassen


class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    market = models.ForeignKey(
        Market, on_delete=models.CASCADE, related_name="products"
    )
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):  # damit in DB anzeigen lassen
        return f"{self.name}"
