from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout
from .forms import *
 
# Create your views here.

def user_login(request):
    context = {}
    if request.method == 'GET':
        context['form'] = AuthenticationForm()
        return render (request, 'accounts/login.html', context)
    else:   
         form = AuthenticationForm(data = request.POST)
         if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('/')
         context['form'] = form
         return render (request, 'accounts/login.html', context)


def register(request):
    context = {}
    if request.method == 'GET':
        context ['form'] = UserRegistrationForm()
        return render (request, 'accounts/register.html', context)
    Form = UserRegistrationForm(request.POST)
    if Form.is_valid():
        user = Form.save(commit=False)
        user.set_password(Form.cleaned_data['password'])
        user.save()
        return redirect('login')
    context ['form'] = Form    
    return render (request, 'accounts/register.html', context)


def user_logout(request):
   logout(request)
   return redirect('/') 