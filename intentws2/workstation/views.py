from django.shortcuts import render,redirect
from workstation.models import Unit, Category
from django.db.models import Q
from workstation.forms import UnitCreateForm, UnitEditForm, CategoryCreateForm

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
        context['categories'] = Category.objects.all()
        
    return render(request, 'home.html', context)

def category_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    else:
        context['user'] = user
        if request.GET:
            category_title = request.GET.get('category')
            category = Category.objects.get(title=category_title)
            units = Unit.objects.filter(category=category)
        context['units'] = units
        context['categories'] = Category.objects.all()
        
    return render(request, 'home.html', context)

def create_category_view(request):
    context = {}
    categories = Category.objects.all
    context['categories'] = categories
    user = request.user
    if user.is_authenticated and user.is_staff:
        form = CategoryCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form = CategoryCreateForm()
            context['form'] = form
            context['unit'] = obj
            return redirect('home')
        return render(request, 'create_category.html', context)
    else:
        return redirect('home')


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
    categories = Category.objects.all
    context['categories'] = categories
    user = request.user
    if user.is_authenticated and user.is_staff:
        form = UnitCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = user
            obj.author = author
            category = request.POST.get('category')
            obj.category = Category.objects.get(title=category)
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
    categories = Category.objects.all
    context['categories'] = categories
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
            category = request.POST.get('category')
            obj.category = Category.objects.get(title=category)
            obj.save()
            context['success_massage'] = "Updated Success"
            unit = obj
    form = UnitEditForm(
        initial = {
            'title': unit.title,
            'category': unit.category,
            'upc': unit.upc,
            'part_number': unit.part_number,
            'details': unit.details,
            'image_url': unit.image_url,
        }
    )
    context['form'] = form
    return render(request, 'edit_unit.html', context)

