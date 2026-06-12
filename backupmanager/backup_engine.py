"""Execucao das rotinas de backup."""

import os
import shutil
from backupmanager.return_codes import (
    OK, 
    ERRO_BACKUP_SEM_ARQUIVOS,
    ERRO_PERFIL_INATIVO,
    ERRO_ORIGEM_INVALIDA,
    ERRO_DESTINO_INVALIDO,
    ERRO_OPERACAO_INVALIDA,
    ERRO_SEM_PERMISSAO,
    ERRO_FALHA_AO_COPIAR,
    ERRO_FALHA_AO_MOVER,
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

def executar_backup(perfil):
    """Executa backup de um perfil validando os dados minimos."""
    resultado = montar_resultado_backup(perfil.get("id"))

    if not perfil.get("ativo", True):
        resultado["status"] = "falha"
        resultado["erros"].append("O perfil esta inativo.")
        return ERRO_PERFIL_INATIVO, resultado

    if not perfil.get("origens"):
        resultado["status"] = "falha"
        resultado["erros"].append("Nenhuma origem configurada.")
        return ERRO_ORIGEM_INVALIDA, resultado

    if not perfil.get("destinos"):
        resultado["status"] = "falha"
        resultado["erros"].append("Nenhum destino configurado.")
        return ERRO_DESTINO_INVALIDO, resultado

    operacao = perfil.get("operacao")
    if operacao not in ("copiar", "mover"):
        resultado["status"] = "falha"
        resultado["erros"].append(f"Operacao configurada invalida: {operacao}")
        return ERRO_OPERACAO_INVALIDA, resultado

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
    """Copia um arquivo da origem para o destino preservando metadados."""
    try:
        shutil.copy2(origem, destino)
        return OK
    except PermissionError:
        return ERRO_SEM_PERMISSAO
    except OSError:
        return ERRO_FALHA_AO_COPIAR


def mover_arquivo(origem, destino):
    """Move um arquivo da origem para o destino."""
    try:
        shutil.move(origem, destino)
        return OK
    except PermissionError:
        return ERRO_SEM_PERMISSAO
    except OSError:
        return ERRO_FALHA_AO_MOVER


def gerar_caminho_destino(arquivo, pasta_destino):
    """Gera caminho de destino para um arquivo abstraindo o sistema operacional."""
    if isinstance(arquivo, dict):
        nome_arquivo = arquivo.get("nome", "")
    else:
        nome_arquivo = os.path.basename(str(arquivo))
        
    caminho_final = os.path.join(pasta_destino, nome_arquivo)
    
    return os.path.normpath(caminho_final)


def criar_pasta_destino_se_necessario(caminho_destino):
    """Cria a pasta de destino quando necessario, incluindo subpastas."""
    try:
        os.makedirs(caminho_destino, exist_ok=True)
        return OK
    except PermissionError:
        return ERRO_SEM_PERMISSAO
    except OSError:
        return ERRO_DESTINO_INVALIDO