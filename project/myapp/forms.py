from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import InventoryItem

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class InventoryItemForm(forms.ModelForm):
     class Meta:
            model = InventoryItem
            fields = ('title','amount', 'date') 
            widgets ={
                'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
                'amount': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
                'date': forms.DateInput(attrs={
                'class': INPUT_CLASSES
            })}

class LogInForm(AuthenticationForm):
        username= forms.CharField(widget=forms.TextInput())
        password= forms.CharField(widget=forms.PasswordInput)

class CodeCheckForm(forms.Form):
    code = forms.CharField(
        max_length=6, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'enter code'})
    )
     

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        username= forms.CharField(widget=forms.TextInput())
        email= forms.CharField(widget=forms.EmailInput)
        password1= forms.CharField(widget=forms.PasswordInput)
        password2= forms.CharField(widget=forms.PasswordInput)
