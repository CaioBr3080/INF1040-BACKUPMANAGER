"""Execucao das rotinas de backup."""

from backupmanager.return_codes import OK, ERRO_BACKUP_SEM_ARQUIVOS


def montar_resultado_backup(perfil_id):
    """Cria o dicionario base de resultado de backup."""
    return {
        "perfil_id": perfil_id,
        "status": "nao_executado",
        "arquivos_processados": 0,
        "arquivos_copiados": 0,
        "arquivos_movidos": 0,
        "erros": [],
    }


def executar_backup(perfil):
    """Executa backup de um perfil. Implementacao completa vira em etapa futura."""
    resultado = montar_resultado_backup(perfil.get("id"))
    return ERRO_BACKUP_SEM_ARQUIVOS, resultado


def executar_backup_multiplos_destinos(perfil, arquivos_validos):
    """Processa arquivos validos para todos os destinos do perfil."""
    del perfil
    del arquivos_validos
    return OK


def processar_arquivo_para_destinos(arquivo, destinos, operacao):
    """Processa um arquivo para uma lista de destinos."""
    del arquivo
    del destinos
    del operacao
    return OK


def copiar_arquivo(origem, destino):
    """Copia um arquivo. Implementacao completa vira em etapa futura."""
    del origem
    del destino
    return OK


def mover_arquivo(origem, destino):
    """Move um arquivo. Implementacao completa vira em etapa futura."""
    del origem
    del destino
    return OK


def gerar_caminho_destino(arquivo, pasta_destino):
    """Gera caminho de destino para um arquivo."""
    del arquivo
    return pasta_destino


def criar_pasta_destino_se_necessario(caminho_destino):
    """Cria a pasta de destino quando necessario."""
    del caminho_destino
    return OK

