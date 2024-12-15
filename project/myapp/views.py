import random
from django.shortcuts import render, redirect, HttpResponse
from .models import InventoryItem
# Create your views here.
from .forms import SignUpForm, LogInForm, CodeCheckForm, InventoryItemForm
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# pretend this is an actual database.
code_database = {}

def SendEmailView(request):
    user_id = request.session.get('user_id')
    error = None
    if user_id not in code_database:
        return redirect('login')

    if request.method == 'POST':
        form = CodeCheckForm(request.POST)
        if form.is_valid():
            entered_code = request.POST['code']
            code = code_database[user_id]
            
            if (entered_code == code['code']):
                user = User.objects.get(pk=user_id)
                login(request, user)
                del code_database[user_id]
                return redirect('home')
        else:
            return render(request, 'codecheck.html', {'error': 'wrong code.'})
    else:
        form = CodeCheckForm()
    return render(request, 'codecheck.html', {'form':form})

def send_email(user, code):
    subject = 'Email authentication from Inventory app'
    message = f'Your code is {code}.'
    from_email = 'cpts327inventoryapp@gmail.com'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

def Home(request):
    return render(request, "home.html")


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LogInForm
    # makes one time pasword
    def make_code(self):
        return str(random.randint(100000, 999999))
    def form_valid(self, form):
        user = form.get_user()        
        code = self.make_code()
        code_database[user.id] = {'code': code}
        send_email(user, code) # send the email.
        self.request.session['user_id'] = user.id
        return redirect('codecheck')

def InventoryItems(request):
    items = InventoryItem.objects.all()
    return render(request, "InventoryItem.html", {"InventoryItems":items})

def SignUp(request):
    if request.method == 'POST':     # form has been submitted
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save() # save the user in database.

            return redirect('/login/')
    else:
        form= SignUpForm()

    return render(request, 'signup.html', {'form':form})

@login_required
def AddItem(request):
    if request.method == 'POST':     # form has been submitted
        form = InventoryItemForm(request.POST)

        if form.is_valid():
            form.save() # save the user in database.

            return redirect('InventoryItem')
    else:
        form= InventoryItemForm()

    return render(request, 'AddItem.html', {'form':form})
