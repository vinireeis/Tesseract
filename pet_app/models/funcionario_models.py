from django.db.models import CharField, DateField, IntegerField
from django.contrib.auth.models import AbstractUser


class Funcionario(AbstractUser):
    CARGO_CHOICES = [
        (1, "Médico Veterinario"),
        (2, "Financeiro"),
        (3, "Atendimento"),
    ]
    nome = CharField(max_length=50, null=False, blank=False)
    nascimento = DateField(null=False, blank=False)
    cargo = IntegerField(choices=CARGO_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.nome
