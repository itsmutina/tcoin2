from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import Customer, Amount
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    balances = Customer.objects.get(name = "wilmot2")
    wilmot2 = balances.balance
    withdraw = balances.withdrawn

    context = {
        'wilmot2':wilmot2,
        'withdraw': withdraw

    }
    return render(request, 'accounts/dashboard.html', context)



def earn(request):
    return render(request, 'accounts/earn.html')

def withdraw(request):
    return render(request, 'accounts/withdraw.html')

def withdrawconfirm(request):
    return render(request, 'accounts/withdrawlconfirm.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else: messages.info(request, 'Invalid crintentials')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')



def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for'  + user)
            return redirect('login')

    context={
        'form':form
    }
    return render(request, 'accounts/register.html', context)

