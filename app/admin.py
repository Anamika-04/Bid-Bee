from django.contrib import admin
from .models import Product, Auction, Bid

admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Bid)
