"""Controle simples de execucao automatica."""

from backupmanager.return_codes import OK

MONITORAMENTO_ATIVO = False


def deve_executar(perfil):
    """Verifica se um perfil deve executar automaticamente."""
    agendamento = perfil.get("agendamento", {})
    if agendamento.get("tipo") == "intervalo":
        return deve_executar_por_intervalo(perfil)
    if agendamento.get("tipo") == "alteracao":
        return deve_executar_por_alteracao(perfil)
    return False


def deve_executar_por_intervalo(perfil):
    """Base para verificacao por intervalo."""
    del perfil
    return False


def deve_executar_por_alteracao(perfil):
    """Base para verificacao por alteracao."""
    del perfil
    return False


def obter_estado_atual_arquivos(perfil):
    """Retorna estado atual de arquivos monitorados."""
    del perfil
    return {}


def comparar_estado_arquivos(estado_antigo, estado_novo):
    """Compara dois estados de arquivos."""
    return estado_antigo != estado_novo


def atualizar_estado_arquivos(perfil):
    """Atualiza o estado de arquivos dentro do perfil."""
    perfil["estado_arquivos"] = obter_estado_atual_arquivos(perfil)
    return OK


def iniciar_monitoramento(perfis, callback_backup):
    """Inicia monitoramento simples. Implementacao completa vira em etapa futura."""
    global MONITORAMENTO_ATIVO
    del perfis
    del callback_backup
    MONITORAMENTO_ATIVO = True
    return OK


def parar_monitoramento():
    """Para monitoramento simples."""
    global MONITORAMENTO_ATIVO
    MONITORAMENTO_ATIVO = False
    return OK

