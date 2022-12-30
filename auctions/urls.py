from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create , name='create'),
    path("listing", views.listing, name = 'listing'),
    path("watchlist", views.watchlist, name = 'watchlist'),
    path("watch", views.watch , name='watch'),
    path("bid", views.bid, name='bid'),
    path("comment", views.comment, name = 'comment'),
    path("listings/<str:name>", views.listings, name = 'listings')
]
