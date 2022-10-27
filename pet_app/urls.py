from .views import funcionario_views, autenticacao_views, cliente_views
from django.urls import path

urlpatterns = [
    path(
        "cadastrar_cliente", cliente_views.cadastrar_cliente, name="cadastrar_cliente"
    ),
    path("listar_clientes", cliente_views.listar_clientes, name="listar_clientes"),
    path(
        "listar_cliente/<int:id>",
        cliente_views.listar_cliente_id,
        name="listar_cliente",
    ),
    path(
        "remover_cliente/<int:id>",
        cliente_views.remover_cliente,
        name="remover_cliente",
    ),
    path(
        "editar_cliente/<int:id>", cliente_views.editar_cliente, name="editar_cliente"
    ),
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
    path(
        "remover_funcionario/<int:id>",
        funcionario_views.remover_funcionario,
        name="remover_funcionario",
    ),
    path(
        "editar_funcionario/<int:id>",
        funcionario_views.editar_funcionario,
        name="editar_funcionario",
    ),
    path("login", autenticacao_views.login_usuario, name="login"),
    path("logout", autenticacao_views.deslogar_usuario, name="logout"),
]
