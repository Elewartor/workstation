from django.shortcuts import render,redirect
from workstation.models import Unit
from django.db.models import Q
from workstation.forms import UnitCreateForm

# Create your views here.

def home_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    else:
        units = Unit.objects.all()
        
        context['user'] = user

        query = ""
        if request.GET:
            query = request.GET.get("q")
            context['query'] = str(query)
            units = get_units_queryset(str(query))

        context['units'] = units
        
    return render(request, 'home.html', context)

def get_units_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        units = Unit.objects.filter(
                Q(title__icontains=q) | 
                Q(upc__icontains=q)
            ).distinct()    
        for unit in units:
            queryset.append(unit)
    return list(set(queryset))

def create_unit_view(request):
    context = {}

    user = request.user
    if user.is_authenticated and user.is_staff:
        form = UnitCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = user
            obj.author = author
            obj.save()
            form = UnitCreateForm()
            context['form'] = form
            return render(request, 'add_unit.html', context)
        else:
            return render(request, 'add_unit.html', context)
    else:
        return redirect('home')