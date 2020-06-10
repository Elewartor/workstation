from django.shortcuts import render, redirect
from workstation.models import Unit
from .models import PrintLog
import os

# Create your views here.

def print_view(request):
    context = {}
    if request.user.is_authenticated:
        if request.GET:
            pk = request.GET.get('pk')
            unit = Unit.objects.get(pk=pk)
            context['unit'] = unit
            return render(request, 'print.html', context)
    else:
        return redirect('home')

def print_boxlabel_view(request):
    if request.user.is_authenticated:
        if request.POST:
            pk = request.POST.get('pk')
            unit = Unit.objects.get(pk=pk)
            user = request.user
            qty = request.POST.get('qty')
            model = unit.title
            upc = unit.upc
            copies = request.POST.get('copies')
            label_type = 'BLL'
            print_log = PrintLog(user=user, unit=unit, copies_printed=copies, label_type=label_type)
            print_log.save()
            command = 'boxlabel.py' + " " + '"' + copies + '"' + " " + '"' + upc + '"' + " " + '"' + qty + '"' + " " + '"' + model + '"'  + " " + '"' + str(print_log.pk) + '"'
            os.system(command)
            

            
            return redirect('home')
    else:
        return redirect('home')

def print_label_view(request):
    if request.user.is_authenticated:
        if request.POST:
            pk = request.POST.get('pk')
            unit = Unit.objects.get(pk=pk)
            user = request.user
            model = unit.title
            upc = unit.upc
            part_number = unit.part_number
            copies = request.POST.get('copies')
            label_type = 'LLL'
            print_log = PrintLog(user=user, unit=unit, copies_printed=copies, label_type=label_type)
            print_log.save()
            command = 'label.py' + " " + '"' + copies + '"' + " " + '"' + upc + '"' + " " + '"' + part_number + '"' + " " + '"' + model + '"'  + " " + '"' + str(print_log.pk) + '"'
            os.system(command)
            

            
            return redirect('home')
    else:
        return redirect('home')

def print_extraboxlabel_view(request):
    if request.user.is_authenticated:
        if request.POST:
            pk = request.POST.get('pk')
            unit = Unit.objects.get(pk=pk)
            user = request.user
            qty = request.POST.get('qty')
            extra = request.POST.get('label_id')
            model = unit.title
            upc = unit.upc
            copies = request.POST.get('copies')
            label_type = 'BLL'
            print_log = PrintLog(user=user, unit=unit, copies_printed=copies, label_type=label_type)
            print_log.save()
            command = 'boxlabelextra' + " " + '"' + copies + '"' + " " + '"' + upc + '"' + " " + '"' + qty + '"' + " " + '"' + extra + '"' + " " + '"' + model + '"'  + " " + '"' + str(print_log.pk) + '"'
            os.system(command)
            

            
            return redirect('home')
    else:
        return redirect('home')