from django import forms
from .models import Propietarios

class PropietarioForm(forms.ModelForm):
    class Meta:
        model=Propietarios
        fields= "__all__"