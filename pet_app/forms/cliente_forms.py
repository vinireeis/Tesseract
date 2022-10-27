from django import forms
from django.forms import DateInput
from ..models import cliente_models


class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente_models.Cliente
        fields = ["nome", "email", "data_nascimento", "cpf", "profissao"]
        widgets = {"data_nascimento": DateInput(attrs={"type": "date"})}
