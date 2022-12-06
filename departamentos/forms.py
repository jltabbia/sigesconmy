from django import forms
from .models import Departamentos

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamentos
        fields= "__all__"