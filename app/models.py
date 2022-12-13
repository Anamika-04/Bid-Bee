from django.db import models
from django.conf import settings
import datetime

class Product(models.Model):
    CATEGORIES = (
        ('ELC', 'Electronics'),
        ('UNI', 'Unique Items'),
        ('RES', 'Real Estate'),
        ('VEH', 'Vehicles'),
        ('OTH', 'Others')
        )
    p_id = models.IntegerField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length = 500)
    quantity = models.IntegerField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES
        )
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)

class Auction(models.Model):
    a_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_price = models.IntegerField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()
    #winner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

class Bid(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()
    bid_amount = models.IntegerField()

    