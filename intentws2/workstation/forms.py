from django import forms

from workstation.models import Unit

class UnitCreateForm(forms.ModelForm):


    class Meta:
        model = Unit
        fields = ('title', 'upc', 'part_number', 'image_url')

        