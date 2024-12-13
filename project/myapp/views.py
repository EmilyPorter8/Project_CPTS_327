from django.shortcuts import render, HttpResponse
from .models import InventoryItem
# Create your views here.

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def InventoryItems(request):
    items = InventoryItem.objects.all()
    return render(request, "InventoryItem.html", {"InventoryItems":items})