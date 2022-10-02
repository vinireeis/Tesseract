from django.db.models import Model, DateTimeField, CharField, IntegerField, ForeignKey
from django.db.models.deletion import CASCADE
from ..models import cliente_models


class TimeStampedModel(Model):
    created_on = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Pet(TimeStampedModel):

    CATEGORIA_PET_CHOICES = (
        ("Ca", "Cachorro"),
        ("Ga", "Gato"),
        ("Pa", "Pássaro"),
        ("Ha", "Hamister"),
    )

    COR_PET_CHOICES = (
        ("Pr", "Preto"),
        ("Br", "Branco"),
        ("Ci", "Cinza"),
        ("Ma", "Malhado"),
        ("Cr", "Creme"),
        ("Mr", "Marrom"),
        ("Am", "Amarelo"),
    )

    GENERO_PET_CHOICES = (
        ("Fe", "Femea"),
        ("Ma", "Macho"),
    )

    nome = CharField(max_length=50, null=False, blank=False)
    idade = IntegerField(blank=False, null=False)
    peso = CharField(max_length=50, null=False, blank=False)
    categoria = CharField(
        max_length=2, choices=CATEGORIA_PET_CHOICES, blank=True, null=True
    )
    cor = CharField(max_length=2, choices=COR_PET_CHOICES, blank=True, null=True)
    raca = CharField(max_length=20, blank=True, null=True)
    genero = CharField(max_length=2, choices=GENERO_PET_CHOICES, blank=True, null=True)
    proprietario = ForeignKey(
        cliente_models.Cliente, on_delete=CASCADE, blank=False, null=False
    )
