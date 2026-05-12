"""Funcoes auxiliares para arquivos e diretorios."""

import os
from pathlib import Path


def caminho_existe(caminho):
    """Verifica se um caminho existe."""
    return Path(caminho).exists()


def caminho_e_diretorio(caminho):
    """Verifica se um caminho existe e e diretorio."""
    return Path(caminho).is_dir()


def listar_arquivos_em_origem(origem):
    """Lista recursivamente arquivos de uma origem."""
    arquivos = []
    for raiz, _, nomes in os.walk(origem):
        for nome in nomes:
            arquivos.append(str(Path(raiz) / nome))
    return arquivos


def listar_arquivos_de_origens(origens):
    """Lista arquivos de varias origens."""
    arquivos = []
    for origem in origens:
        arquivos.extend(listar_arquivos_em_origem(origem))
    return arquivos


def obter_extensao(caminho):
    """Retorna a extensao de um arquivo em minusculas."""
    return Path(caminho).suffix.lower()


def obter_metadados_arquivo(caminho):
    """Monta o dicionario de metadados de um arquivo."""
    caminho_path = Path(caminho)
    estatisticas = caminho_path.stat()
    return {
        "caminho": str(caminho_path),
        "nome": caminho_path.name,
        "extensao": obter_extensao(caminho_path),
        "tamanho": estatisticas.st_size,
        "data_modificacao": estatisticas.st_mtime,
    }


def arquivo_atende_restricoes(arquivo, restricoes):
    """Verifica se um arquivo passa por todas as restricoes."""
    return (
        atende_restricao_extensao(arquivo, restricoes)
        and atende_restricao_nome(arquivo, restricoes)
        and atende_restricao_tamanho(arquivo, restricoes)
        and atende_restricao_data_modificacao(arquivo, restricoes)
    )


def atende_restricao_extensao(arquivo, restricoes):
    """Verifica filtro por extensao."""
    extensoes = restricoes.get("extensoes_permitidas", [])
    if not extensoes:
        return True
    extensoes = [ext.lower() for ext in extensoes]
    return arquivo.get("extensao", "").lower() in extensoes


def atende_restricao_nome(arquivo, restricoes):
    """Verifica filtro por trecho no nome."""
    trecho = restricoes.get("nome_contem", "")
    if not trecho:
        return True
    return trecho.lower() in arquivo.get("nome", "").lower()


def atende_restricao_tamanho(arquivo, restricoes):
    """Verifica filtros por tamanho minimo e maximo."""
    tamanho = arquivo.get("tamanho", 0)
    tamanho_min = restricoes.get("tamanho_min", 0)
    tamanho_max = restricoes.get("tamanho_max")
    if tamanho < tamanho_min:
        return False
    if tamanho_max is not None and tamanho > tamanho_max:
        return False
    return True


def atende_restricao_data_modificacao(arquivo, restricoes):
    """Base para filtro de data; sera refinada em etapa futura."""
    del arquivo
    del restricoes
    return True


def verificar_permissao_leitura(caminho):
    """Verifica permissao de leitura."""
    return os.access(caminho, os.R_OK)


def verificar_permissao_escrita(caminho):
    """Verifica permissao de escrita."""
    return os.access(caminho, os.W_OK)

