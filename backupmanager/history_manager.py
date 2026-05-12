"""Gerenciamento do historico de backups."""

import uuid
from datetime import datetime

from backupmanager.return_codes import OK


def criar_registro_historico(perfil_id, resultado):
    """Cria um registro de historico a partir do resultado do backup."""
    return {
        "id": "hist_" + uuid.uuid4().hex[:8],
        "perfil_id": perfil_id,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": resultado.get("status", "desconhecido"),
        "arquivos_processados": resultado.get("arquivos_processados", 0),
        "arquivos_copiados": resultado.get("arquivos_copiados", 0),
        "arquivos_movidos": resultado.get("arquivos_movidos", 0),
        "erros": resultado.get("erros", []),
    }


def registrar_backup(historico, perfil_id, resultado):
    """Adiciona uma execucao ao historico."""
    historico.append(criar_registro_historico(perfil_id, resultado))
    return OK


def consultar_historico_por_perfil(historico, perfil_id):
    """Lista registros de historico de um perfil."""
    registros = [registro for registro in historico if registro.get("perfil_id") == perfil_id]
    return OK, registros


def listar_historico(historico):
    """Retorna todos os registros de historico."""
    return OK, historico


def limpar_historico_perfil(historico, perfil_id):
    """Remove registros de historico de um perfil."""
    historico[:] = [registro for registro in historico if registro.get("perfil_id") != perfil_id]
    return OK


def limpar_todo_historico(historico):
    """Remove todos os registros de historico."""
    historico.clear()
    return OK

