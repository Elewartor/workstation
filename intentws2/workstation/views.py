from django.shortcuts import render,redirect
from workstation.models import Unit

# Create your views here.

def home_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    else:
        context = {}
        units = Unit.objects.all()
        context['units'] = units
        context['user'] = user
    return render(request, 'home.html', context)