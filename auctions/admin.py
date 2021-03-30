from django.contrib import admin
from .models import User, Category, Auction, Bid


class AuctionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'starting_price']

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'last_login']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class BidAdmin(admin.ModelAdmin):
    list_display = ['myproduct', 'date_bid', 'user', 'bid_price']

admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid, BidAdmin)
