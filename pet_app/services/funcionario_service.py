from ..models import funcionario_models


def listar_funcionarios():
    funcionarios = funcionario_models.Funcionario.objects.all()
    return funcionarios


def cadastrar_funcionario(funcionario):
    funcionario_models.Funcionario.objects.create(
        nome=funcionario.nome,
        nascimento=funcionario.nascimento,
        cargo=funcionario.cargo,
        username=funcionario.username,
        password=funcionario.password,
    )


def listar_funcionario_id(id):
    return funcionario_models.Funcionario.objects.get(id=id)


def remover_funcionario(funcionario):
    funcionario.delete()


def editar_funcionario(funcionario, funcionario_novo):
    funcionario.nome = funcionario_novo.nome
    funcionario.nascimento = funcionario_novo.nascimento
    funcionario.cargo = funcionario_novo.cargo
    funcionario.username = funcionario_novo.username
    funcionario.password = funcionario_novo.password

    funcionario.save(force_update=True)
