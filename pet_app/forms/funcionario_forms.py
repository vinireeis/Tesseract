from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm
from ..models import funcionario_models


class FuncionarioForm(UserCreationForm):
    class Meta:
        model = funcionario_models.Funcionario
        fields = UserCreationForm.Meta.fields + (
            "nome",
            "nascimento",
            "cargo",
        )
        widgets = {"nascimento": DateInput(attrs={"type": "date"})}
