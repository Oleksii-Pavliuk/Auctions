from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django import forms
import datetime

from .models import User, Category,Lot


#List of categories
categories = []
for category in Category.objects.all():
    categories.append((category.name , category.name))

#Form for new listings
class Listing(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'name':'name', 'class':'namefield'}))
    category = forms.ChoiceField(choices= categories, widget=forms.Select(attrs={'name': 'Category', 'class': 'dropdown'}))
    price = forms.IntegerField(label='Price:', min_value= 0, widget=forms.NumberInput(attrs={'name':'price', 'class': 'pricefield'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'name':'description','class':'textarea'}))


#Index page
def index(request):
    return render(request, "auctions/index.html",{
        'lots': Lot.objects.all(),
        'path': 'auctions/'
    })



#Create listing function
@login_required
def create(request):
    if request.method == 'POST':
        form = Listing(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            name = form['name']
            category = form['category']
            price = form['price']
            description = form['description']
            image = request.FILES['image']
            new_lot = Lot(
                user = User.objects.get(username = (request.user.username)),
                name = name,price = price,
                category = Category.objects.get(name = (category)), 
                image = image,
                description = description, 
                active = True, 
                date = datetime.datetime.now())
            new_lot.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'auctions/listing.html', {
            'form': Listing
        })


#Show listing function
def listing(request):

    id = request.GET['id']

    lot = Lot.objects.get(pk = id)

    return render(request, 'auctions/lot.html',{
        'lot': lot
    })











#Login page
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


#Logout function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


#Register page
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
