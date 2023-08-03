from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Listing, Comments, Bids, Categories


def index(request):
    return render(request, "auctions/index.html")


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


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
    
def active_listing(request):
    return render(request, "auctions/active.hmtl")

# @login_required
def create_listing(request):
    context = {}
    form = Listing(request.POST, request.FILES)
    
    if request.method == "POST":
        if form.is_valid():
            try:
                title = request.POST["title"]
                description = request.POST["description"]
                starting_bid = request.POST["price"]
                image = request.POST.get("image", False)
                category = Categories.objects.get(pk=(request.POST["category"]))
                activate = Listing.objects.create( 
                                                  title = title,
                                                  description = description,
                                                  price = starting_bid,
                                                  image = image,
                                                  categories = category)
                activate.save()
                print(activate)
                
            except IntegrityError:
                return render(request, "auctions/create.html", {
                    "message": "Please fill in required fields."
                })
        
        return HttpResponseRedirect(reverse("active"))
    else:
        return render(request, "auctions/create.html", {
            "categories": Categories.objects.all()
        })
    

def category_view(request):
    return render(request, "auctions/categories.html")

def active_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "auctions/active.html", {
        "listing": listing
    })
    