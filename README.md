Projeto em Python para gerenciar perfis de backup de arquivos, com suporte a copia ou movimentação de arquivos, filtros e historico de execução.

## Recursos

- Cadastro de perfis de backup.
- Configuração de pastas de origem e destino.
- Operções de copiar ou mover arquivos.
- Filtros por nome, extensao, tamanho e data de modificacao.
- Historico das execucoes.
- Testes automatizados com `pytest`.

## Como Executar

Na pasta do projeto, execute:

```bash
python -m backupmanager.main
```

Para abrir a interface visual de preview:

```bash
python preview_interface.py
```

O preview usa `customtkinter`. Caso nao esteja instalado:

```bash
pip install customtkinter
```

## Testes

Para rodar os testes:

```bash
pytest
```

## Estrutura

```text
backupmanager/        Codigo principal do sistema
tests/                Testes automatizados
data/                 Arquivos locais de configuracao e historico
preview_interface.py  Prototipo visual da interface
```

## Observação

Os arquivos JSON dentro de `data/` sao dados locais de uso da aplicaçãao e nao são versionados.
