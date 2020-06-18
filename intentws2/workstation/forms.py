from django import forms

from workstation.models import Unit

class UnitCreateForm(forms.ModelForm):


    class Meta:
        model = Unit
        fields = ('title', 'upc', 'part_number', 'details', 'image_url')

class UnitEditForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('title', 'upc', 'part_number', 'details', 'image_url')

    def save(self, commit=True):
        unit = self.instance
        unit.title = self.cleaned_data['title']
        unit.upc = self.cleaned_data['upc']
        unit.part_number = self.cleaned_data['part_number']
        unit.details = self.cleaned_data['details']
        unit.image_url = self.cleaned_data['image_url']

        if commit:
            unit.save()
        return unit