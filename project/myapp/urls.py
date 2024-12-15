from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path("", views.Home, name = "home"),
    path("signup/", views.SignUp, name = "signup"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("email/", views.SendEmailView, name = "email"),
    path("codecheck/", views.SendEmailView, name = "codecheck"), # for chekcing the code.
    path("InventoryManager/", views.InventoryItems, name = "InventoryItem")
]