from django import forms
from usuario.models import Usuario
from .models import Edificios

class EdificoForm(forms.ModelForm):
    class Meta:
        model=Edificios
        fields= "__all__"