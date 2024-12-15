from django.shortcuts import render, redirect, HttpResponse
from .models import InventoryItem
# Create your views here.
from .forms import SignUpForm
from django.core.mail import send_mail

def send_email_view(request):
    if request.method == 'POST':
        send_mail(
            'Test Subject',
            'This is a test email from Django!',
            'cpts327inventoryapp@gmail.com',  # From email
            ['emily.l.porter@wsu.edu'],  # To email
            fail_silently=False,
        )
        return render(request, 'email_sent.html')  # A confirmation template
    return render(request, 'send_email.html')  # A form to trigger the email


def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def InventoryItems(request):
    items = InventoryItem.objects.all()
    return render(request, "InventoryItem.html", {"InventoryItems":items})

def signup(request):
    if request.method == 'POST':     # form has been submitted
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save() # save the user in database.

            return redirect('/login/')
    else:
        form= SignUpForm()

    return render(request, 'signup.html', {'form':form})