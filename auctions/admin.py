from django.contrib import admin
from .models import User, Category, Auction, Bid



admin.site.register(User)
admin.site.register(Category)
admin.site.register(Auction)
admin.site.register(Bid)
