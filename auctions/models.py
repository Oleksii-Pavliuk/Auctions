from django.contrib.auth.models import AbstractUser
from django.db import models


#user model
class User(AbstractUser):
    pass




#Category model
class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name



#Lot model
class Lot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher')
    name = models.CharField(max_length=100)
    price = models.DecimalField( max_digits=8 ,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.FileField(upload_to='auctions/static/uploads/')
    description = models.TextField()
    date = models.DateTimeField()
    active = models.BooleanField()
    winner = models.CharField(max_length= 100)

    def __str__(self):
        return f'{self.name} for {self.price} listed on {self.date} by {self.user} in category: {self.category}'




# Bids model
class Bid(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='item')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='bidder')
    price = models.DecimalField(max_digits=8 ,decimal_places=2)

    def __str__(self):
        return f'{self.price} for {self.lot} from {self.user}'


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watcher')
    item = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='watchitem')


#Comment model 
class Comment(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='lot')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return f'{self.user} at {self.date} commented "{self.comment}" about {self.lot}'
