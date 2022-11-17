from django import forms
from .models import Movimientos

class MovimientoForm(forms.ModelForm):
    class Meta:
        model=Movimientos
        fields= "__all__"