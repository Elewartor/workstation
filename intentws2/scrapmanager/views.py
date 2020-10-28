from django.shortcuts import render, redirect
from workstation.models import Unit, Category
from scrapmanager.models import CategoryQuestions, ScrapRecord, ScrapRecordToQuestion, Questions
from django.db.models import Count
import os
from django.db.models import Q
# Create your views here.

def create_scrap_record_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    else:
        context = {}
        context['categories'] = Category.objects.all()
        context['user'] = user

        if request.GET:
            pk = request.GET.get('pk')
            unit = Unit.objects.get(pk=pk)
            if not unit.category:
                return redirect('home')
            else:
                category = Category.objects.get(title=unit.category.title)
                questions = CategoryQuestions.objects.filter(category=category)
                context['questions'] = questions
                context['unit'] = unit

        if request.POST:
            user = request.user
            unit = Unit.objects.get(pk=request.POST.get('unit_pk'))
            scrap_record = ScrapRecord(scrap_author=user, scrap_unit=unit)
            scrap_record.save()

            for key in request.POST:
                if key == 'unit_pk' or key == 'csrfmiddlewaretoken':
                    continue

                question = Questions.objects.get(pk=key)
                answer = request.POST.get(key)
                scrap_record_to_question = ScrapRecordToQuestion(scrap_record=scrap_record, question=question, answer=answer)
                scrap_record_to_question.save()

            command = 'scrap_record.py' + " " + '"' + scrap_record.pk + '"'
            os.system(command)

            context['record'] = scrap_record   

            return render(request, 'result.html', context)
            

        return render(request, 'create_scrap_record.html', context)

def manager_view(request):
    if not request.user.is_authenticated and not request.user.is_stuff:
        return redirect('home')
    else:
        context = {}
        data_set = []
        scrap_records = ScrapRecord.objects.all()
        if request.GET:
            query = request.GET.get('scrap_search')
            scrap_records = ScrapRecord.objects.filter(Q(scrap_unit__title__contains=query) | Q(pk__contains=query))

        for record in scrap_records:
            data = {}
            scrap_record_to_question = ScrapRecordToQuestion.objects.filter(scrap_record=record)
            data['record'] = record
            data['scrap_record_to_question'] = scrap_record_to_question
            data_set.append(data)
        
        # unit counter
        counter_set = []
        field_name = 'scrap_unit'
        for item in ScrapRecord.objects.values(field_name).order_by(field_name).annotate(the_count=Count(field_name)):
            data = {}
            unit = Unit.objects.get(pk=item['scrap_unit'])
            data['unit_title'] = unit.title
            data['unit_count'] = item['the_count']
            counter_set.append(data)


        context['total_value'] = scrap_records.__len__
        context['categories'] = Category.objects.all()
        context['counter_set'] = counter_set
        context['data_set'] = data_set
        return render(request, 'manager.html', context)

def remove_scrap_record_view(request):
    if not request.user.is_authenticated and not request.user.is_stuff:
        return redirect('home')
    else:
        if request.POST:
            record_pk = request.POST.get('remove')
            scrap_record = ScrapRecord.objects.get(pk=record_pk)
            scrap_record.delete()
        return redirect('manager')
