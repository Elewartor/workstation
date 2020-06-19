from django.shortcuts import render, redirect
from workstation.models import Unit
from .models import PrintLog
import os

# Create your views here.

def print_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if request.GET:
            pk = request.GET.get('pk')
            unit = Unit.objects.get(pk=pk)
            context['unit'] = unit
            context['toggle'] = 'lll'
        if request.POST:
            if 'box_label' == request.POST['label']:
                pk = request.POST.get('pk')
                unit = Unit.objects.get(pk=pk)
                qty = request.POST.get('qty')
                copies = request.POST.get('copies')
                context['result_massage'] = print_boxlabel(user, unit, qty, copies)
                context['toggle'] = 'bll'
                context['unit'] = unit
                
            if 'unit_label' == request.POST['label']:
                pk = request.POST.get('pk')
                unit = Unit.objects.get(pk=pk)
                copies = request.POST.get('copies')
                context['result_massage'] = print_label(user, unit, copies)
                context['toggle'] = 'lll'
                context['unit'] = unit

            if 'extra_box_label' == request.POST['label']:
                pk = request.POST.get('pk')
                unit = Unit.objects.get(pk=pk)
                copies = request.POST.get('copies')
                qty = request.POST.get('qty')
                extra = request.POST.get('extra')
                context['result_massage'] = print_extraboxlabel(user, unit, qty, extra, copies)
                context['toggle'] = 'ebl'
                context['unit'] = unit

        return render(request, 'print.html', context)
    else:
        return redirect('home')

def print_extraboxlabel(user, unit, qty, extra, copies):
    model = unit.title
    upc = unit.upc
    label_type = 'EBL'
    print_log = PrintLog(user=user, unit=unit, copies_printed=copies, label_type=label_type)
    print_log.save()
    command = 'boxlabelextra.py' + " " + '"' + copies + '"' + " " + '"' + upc + '"' + " " + '"' + qty + '"' + " " + '"' + extra + '"' + " " + '"' + model + '"'  + " " + '"' + str(print_log.pk) + '"'
    os.system(command)

    return "Extra Box Label"

def print_boxlabel(user, unit, qty, copies):
    model = unit.title
    upc = unit.upc
    label_type = 'BLL'
    print_log = PrintLog(user=user, unit=unit, copies_printed=copies, label_type=label_type)
    print_log.save()
    command = 'boxlabel.py' + " " + '"' + copies + '"' + " " + '"' + upc + '"' + " " + '"' + qty + '"' + " " + '"' + model + '"'  + " " + '"' + str(print_log.pk) + '"'
    os.system(command)

    return "Box Label"

def print_label(user, unit, copies):
    model = unit.title
    upc = unit.upc
    part_number = unit.part_number
    label_type = 'LLL'
    print_log = PrintLog(user=user, unit=unit, copies_printed=copies, label_type=label_type)
    print_log.save()
    command = 'label.py' + " " + '"' + copies + '"' + " " + '"' + upc + '"' + " " + '"' + part_number + '"' + " " + '"' + model + '"'  + " " + '"' + str(print_log.pk) + '"'
    os.system(command)

    return "Unit Label"

