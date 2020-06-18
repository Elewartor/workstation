from django.shortcuts import render,redirect
from workstation.models import Unit
from django.db.models import Q
from workstation.forms import UnitCreateForm, UnitEditForm

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
            context['success_massage'] = 'Created Success'
            context['unit'] = obj
        return render(request, 'add_unit.html', context)
    else:
        return redirect('home')
        
def edit_unit_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated and user.is_staff:
        redirect('home')
    if request.GET:
        unit_pk = request.GET.get('pk')
        unit = Unit.objects.get(pk=unit_pk)
        context['unit_pk'] = unit_pk
    if request.POST:
        unit_pk = request.POST.get('pk')
        unit = Unit.objects.get(pk=unit_pk)
        form = UnitEditForm(request.POST or None, instance=unit)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_massage'] = "Updated Success"
            unit = obj
    form = UnitEditForm(
        initial = {
            'title': unit.title,
            'upc': unit.upc,
            'part_number': unit.part_number,
            'details': unit.details,
            'image_url': unit.image_url,
        }
    )
    context['form'] = form
    return render(request, 'edit_unit.html', context)

