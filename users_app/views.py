from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm
from django.contrib import messages

def register(request):
    """This method takes in a request an if user is registering the POST 
    condition is exceuted else we just display the registration form.
    """
    if request.method == 'POST':
        # Creating an instance of our class
        register_form = CustomRegistrationForm(request.POST)
        # Checking if the submitted info is valid
        if register_form.is_valid():
            # We save the info in our database
            register_form.save()
            # Display a success message
            messages.success(request,("New user registered successfully! Login to get started."))
            return redirect('register')
    else:
        # return HttpResponse("<h1>Welcome to our user application.</h1>")
        # An instance of our user creation form class
        register_form = CustomRegistrationForm()
        #              request,    template,          context
        #                 ^           ^                 ^
        #                 |           |                 |
    return render(request, 'register.html', {'register_form':register_form})
    
