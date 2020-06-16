from django import forms

from workstation.models import Unit

class UnitCreateForm(forms.ModelForm):


    class Meta:
        model = Unit
        fields = ('title', 'upc', 'part_number', 'details', 'image_url')

    def clean_details(self):
        string = self.cleaned_data['details']
        
        if string[-1]==';':
            string = string[:-1]
        result = ""
        splited = string.replace("; ", ";").split(";")
        for line in splited:
            splited_line = line.split(": ")
            name = splited_line[0]
            value = splited_line[1]
            result = result + "<li class='list-group-item'>" + "<b>" + name + ": </b>" + value + "</li>"     
        
        return result

        