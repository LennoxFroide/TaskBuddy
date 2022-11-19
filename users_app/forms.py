# This file is to help us add extra functionality to the django form
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    #Adding email address field to our form
    email = forms.EmailField(required=True)

    # Meta class is important to configure forms
    class Meta:
        # Indicating which table it should be savedd to
        model = User
        # Fields in our form
        # The order that we have them here matters for our form
        fields = ['username','email','password1','password2']
