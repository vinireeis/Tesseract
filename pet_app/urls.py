from .views import funcionario_views
from django.urls import path

urlpatterns = [
    path(
        "cadastrar_funcionario",
        funcionario_views.inserir_funcionario,
        name="cadastrar_funcionario",
    ),
    path(
        "listar_funcionarios",
        funcionario_views.listar_funcionarios,
        name="listar_funcionarios",
    ),
]
