from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.contrib import messages

# Create your views here.
def iregister(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        name = request.POST['name']
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'welcome new user!!')
            return redirect('login')
            
    else:
        form = UserCreationForm
        return render(request, 'users/register.html', {'form':form})
    
def ilogin(request):
    form = UserCreationForm
    return render(request, 'users/login.html')