from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import AccountAuthenticationForm

# Create your views here.

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'account/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')