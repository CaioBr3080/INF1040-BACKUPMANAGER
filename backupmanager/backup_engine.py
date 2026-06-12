"""Execucao das rotinas de backup."""

from pathlib import Path

from backupmanager.return_codes import (
    OK,
    ERRO_BACKUP_SEM_ARQUIVOS,
    ERRO_DADOS_INVALIDOS,
    ERRO_DESTINO_INVALIDO,
    ERRO_OPERACAO_INVALIDA,
    ERRO_ORIGEM_INVALIDA,
)


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


def validar_perfil_para_backup(perfil):
    """Valida os dados minimos necessarios para executar backup."""
    if not isinstance(perfil, dict):
        return ERRO_DADOS_INVALIDOS

    origens = perfil.get("origens", [])
    destinos = perfil.get("destinos", [])
    operacao = perfil.get("operacao", "copiar")

    if not isinstance(origens, list) or len(origens) == 0:
        return ERRO_ORIGEM_INVALIDA
    if not isinstance(destinos, list) or len(destinos) == 0:
        return ERRO_DESTINO_INVALIDO
    if operacao not in ("copiar", "mover"):
        return ERRO_OPERACAO_INVALIDA

    return OK


def executar_backup(perfil):
    """Executa backup de um perfil. Implementacao completa vira em etapa futura."""
    perfil_id = perfil.get("id") if isinstance(perfil, dict) else None
    resultado = montar_resultado_backup(perfil_id)

    codigo_validacao = validar_perfil_para_backup(perfil)
    if codigo_validacao != OK:
        resultado["status"] = "erro"
        resultado["erros"].append("Perfil invalido para backup.")
        return codigo_validacao, resultado

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
    if not isinstance(arquivo, dict) or not pasta_destino:
        return None

    nome = arquivo.get("nome")
    caminho_origem = arquivo.get("caminho")

    if not nome and caminho_origem:
        nome = Path(caminho_origem).name
    if not nome:
        return None

    return str(Path(pasta_destino) / nome)


def criar_pasta_destino_se_necessario(caminho_destino):
    """Cria a pasta de destino quando necessario."""
    del caminho_destino
    return OK
