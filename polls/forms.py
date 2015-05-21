from django import forms
from models import TextoDeEntrada

class TextoEntradaForm(forms.ModelForm):
   class Meta:
      model = TextoDeEntrada