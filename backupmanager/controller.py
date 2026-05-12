"""Camada de controle entre interface e modulos internos."""

from backupmanager import history_manager, perfil_manager, storage
from backupmanager.return_codes import OK

ESTADO = {
    "perfis": [],
    "historico": [],
    "config": {},
}


def inicializar_aplicacao():
    """Carrega dados iniciais da aplicacao."""
    _, ESTADO["perfis"] = storage.carregar_perfis()
    _, ESTADO["historico"] = storage.carregar_historico()
    _, ESTADO["config"] = storage.carregar_configuracoes()
    return OK


def criar_novo_perfil(nome):
    """Cria um perfil e salva a lista atualizada."""
    codigo, perfil = perfil_manager.criar_perfil(nome)
    if codigo != OK:
        return codigo, None

    ESTADO["perfis"].append(perfil)
    storage.salvar_perfis(ESTADO["perfis"])
    return OK, perfil


def obter_perfis():
    """Retorna todos os perfis."""
    return perfil_manager.listar_perfis(ESTADO["perfis"])


def obter_perfil_por_id(perfil_id):
    """Retorna um perfil pelo id."""
    return perfil_manager.consultar_perfil(ESTADO["perfis"], perfil_id)


def salvar_perfil_editado(perfil):
    """Salva os dados atuais de perfis."""
    del perfil
    return storage.salvar_perfis(ESTADO["perfis"])


def excluir_perfil_por_id(perfil_id):
    """Exclui um perfil e persiste a lista."""
    codigo = perfil_manager.excluir_perfil(ESTADO["perfis"], perfil_id)
    if codigo == OK:
        storage.salvar_perfis(ESTADO["perfis"])
    return codigo


def adicionar_origem_ao_perfil(perfil_id, caminho):
    """Adiciona origem a um perfil."""
    codigo = perfil_manager.adicionar_origem(ESTADO["perfis"], perfil_id, caminho)
    if codigo == OK:
        storage.salvar_perfis(ESTADO["perfis"])
    return codigo


def remover_origem_do_perfil(perfil_id, caminho):
    """Remove origem de um perfil."""
    codigo = perfil_manager.remover_origem(ESTADO["perfis"], perfil_id, caminho)
    if codigo == OK:
        storage.salvar_perfis(ESTADO["perfis"])
    return codigo


def adicionar_destino_ao_perfil(perfil_id, caminho):
    """Adiciona destino a um perfil."""
    codigo = perfil_manager.adicionar_destino(ESTADO["perfis"], perfil_id, caminho)
    if codigo == OK:
        storage.salvar_perfis(ESTADO["perfis"])
    return codigo


def remover_destino_do_perfil(perfil_id, caminho):
    """Remove destino de um perfil."""
    codigo = perfil_manager.remover_destino(ESTADO["perfis"], perfil_id, caminho)
    if codigo == OK:
        storage.salvar_perfis(ESTADO["perfis"])
    return codigo


def definir_restricoes_do_perfil(perfil_id, restricoes):
    """Define restricoes de um perfil."""
    codigo = perfil_manager.alterar_restricoes(ESTADO["perfis"], perfil_id, restricoes)
    if codigo == OK:
        storage.salvar_perfis(ESTADO["perfis"])
    return codigo


def definir_agendamento_do_perfil(perfil_id, agendamento):
    """Define agendamento de um perfil."""
    codigo = perfil_manager.alterar_agendamento(ESTADO["perfis"], perfil_id, agendamento)
    if codigo == OK:
        storage.salvar_perfis(ESTADO["perfis"])
    return codigo


def executar_backup_do_perfil(perfil_id):
    """Executa backup manual de um perfil. Completo em etapa futura."""
    del perfil_id
    return OK


def consultar_historico_do_perfil(perfil_id):
    """Consulta historico de um perfil."""
    return history_manager.consultar_historico_por_perfil(ESTADO["historico"], perfil_id)

