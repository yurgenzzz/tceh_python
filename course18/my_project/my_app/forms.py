from django import forms
from django.core.exceptions import ValidationError


class MyForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField()

    def clean_name(self):
        """auto magic of form validation
        """
        name = self.cleaned_data['name']
        if len(name) <= 3:
            raise ValidationError('Name is too short')
        return name

    def clean(self):
        print('Cleaning self')
        if self.cleaned_data.get('name', None) == 'Ivan':
            raise ValidationError('NOOOO!')

        return self.cleaned_data
