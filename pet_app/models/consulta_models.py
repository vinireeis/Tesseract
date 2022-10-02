from django.db.models import Model, ForeignKey, DateField, TextField, CharField
from django.db.models.deletion import CASCADE
from pet_app.models.pet_models import Pet


class ConsultaPet(Model):
    DOUTOR_CHOICES = (
        ("Ma", "Maria Lima"),
        ("Fc", "Fernanda Cardoso Lira"),
        ("Af", "Amanda Finamor"),
        ("Vm", "Victoria Misson"),
        ("As", "Amanda dos Santos Silva"),
        ("Cv", "Cássia Vasconcellos"),
        ("Rp", "Regina Elis Pascoal"),
    )

    ESPECIALIDADES_CHOICES = (
        ("Cg", "Clinico Geral"),
        ("Cd", "Cardiologia"),
        ("De", "Dermatologia"),
        ("Fi", "Fisioterapia"),
        ("He", "Hematologia"),
        ("Ne", "Neurologia"),
        ("Or", "Ortopedia"),
    )

    pet = ForeignKey(Pet, on_delete=CASCADE, null=False, blank=False)
    data = DateField(null=False, blank=False, auto_now_add=True)
    doutor = CharField(max_length=2, choices=DOUTOR_CHOICES, blank=True, null=True)
    motivo_consulta = CharField(max_length=200, null=False, blank=False)
    medicamento_atual = TextField(null=False, blank=False)
    medicamentos_prescritos = TextField(null=False, blank=False)
    exames = TextField(null=False, blank=False)
    especialidade = CharField(
        max_length=2, choices=ESPECIALIDADES_CHOICES, blank=True, null=True
    )
    observacoes = TextField(null=False, blank=False)
