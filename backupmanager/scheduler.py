"""Controle simples de execucao automatica."""

import time
import threading
from backupmanager import file_utils
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
    """Verifica se houve mudanca nos arquivos monitorados."""
    if not perfil.get("ativo", True):
        return False
        
    estado_antigo = perfil.get("estado_arquivos", {})
    estado_novo = obter_estado_atual_arquivos(perfil)
    
    return comparar_estado_arquivos(estado_antigo, estado_novo)


def obter_estado_atual_arquivos(perfil):
    """Retorna estado atual de arquivos monitorados gerando assinaturas unicas."""
    estado = {}
    origens = perfil.get("origens", [])
    
    arquivos = file_utils.listar_arquivos_de_origens(origens)
    
    for caminho in arquivos:
        try:
            metadados = file_utils.obter_metadados_arquivo(caminho)
            assinatura = f"{metadados.get('tamanho')}_{metadados.get('data_modificacao')}"
            estado[caminho] = assinatura
        except OSError:
            pass
            
    return estado


def comparar_estado_arquivos(estado_antigo, estado_novo):
    """Compara dois estados de arquivos."""
    return estado_antigo != estado_novo


def atualizar_estado_arquivos(perfil):
    """Atualiza o estado de arquivos dentro do perfil."""
    perfil["estado_arquivos"] = obter_estado_atual_arquivos(perfil)
    return OK


def iniciar_monitoramento(perfis, callback_backup):
    """Inicia monitoramento em background sem travar a interface."""
    global MONITORAMENTO_ATIVO
    
    if MONITORAMENTO_ATIVO:
        return OK

    MONITORAMENTO_ATIVO = True

    def loop_monitoramento():
        """Função que rodará em paralelo na thread."""
        while MONITORAMENTO_ATIVO:
            for perfil in perfis:
                if deve_executar(perfil):
                    callback_backup(perfil.get("id"))
            
            time.sleep(5)

    thread = threading.Thread(target=loop_monitoramento, daemon=True)
    thread.start()

    return OK


def parar_monitoramento():
    """Para monitoramento simples."""
    global MONITORAMENTO_ATIVO
    MONITORAMENTO_ATIVO = False
    return OK