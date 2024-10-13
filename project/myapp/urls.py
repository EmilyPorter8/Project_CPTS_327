from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("InventoryManager/", views.InventoryItems, name = "InventoryItem.html")
]