from django.contrib import admin

# Register your models here.
from .models import Category, Lot, User, Comment, Bid, Watchlist

admin.site.register(Category)
admin.site.register(Lot)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Watchlist)