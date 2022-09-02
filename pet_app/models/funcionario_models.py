from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Funcionario(AbstractUser):
    CARGO_CHOICES = [
        (1, "Médico Veterinario"),
        (2, "Financeiro"),
        (3, "Atendimento"),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=True, blank=False)
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=True, blank=False)

    def __str__(self):
        return self.nome


Funcionario = get_user_model()
