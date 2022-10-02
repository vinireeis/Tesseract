from django.db.models import (
    CharField,
    Model,
    DateTimeField,
    EmailField,
    ForeignKey,
    DateField,
)
from django.db.models.deletion import CASCADE
from django_localflavor_br.br_states import STATE_CHOICES


class TimeStampedModel(Model):
    created_on = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class EnderecoCliente(Model):
    rua = CharField(max_length=50, null=False, blank=False)
    cidade = CharField(max_length=30, null=False, blank=False)
    estado = CharField(max_length=2, choices=STATE_CHOICES)


class Cliente(TimeStampedModel):
    nome = CharField(max_length=100, null=False, blank=False)
    email = EmailField(null=False, blank=False)
    endereco = ForeignKey(EnderecoCliente, on_delete=CASCADE)
    cpf = CharField(max_length=14, unique=True, null=False, blank=True)
    data_nascimento = DateField(null=False, blank=False)
    profissao = CharField(max_length=25, null=False, blank=False)
