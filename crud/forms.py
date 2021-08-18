from django import forms
from crud.models import crudst
class stform(forms.ModelForm):
    class Meta:
        model=crudst
        fields=['stname', 'stemail', 'stgrade']

