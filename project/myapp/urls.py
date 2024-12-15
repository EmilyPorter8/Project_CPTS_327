from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LogInForm

urlpatterns = [
    path("", views.home, name = "home"),
    path("signup/", views.signup, name = "signup"),
    path("login/", auth_views.LoginView.as_view(template_name = 'login.html', authentication_form=LogInForm), name = "login"),
    path("email/", views.send_email_view, name = "email"),
    path("InventoryManager/", views.InventoryItems, name = "InventoryItem")
]