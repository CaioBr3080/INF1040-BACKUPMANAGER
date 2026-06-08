# BackupManager

Projeto em Python para gerenciar perfis de backup de arquivos, com suporte a copia ou movimentacao de arquivos, filtros e historico de execucao.

## Recursos

- Cadastro de perfis de backup.
- Configuracao de pastas de origem e destino.
- Operacoes de copiar ou mover arquivos.
- Filtros por nome, extensao, tamanho e data de modificacao.
- Historico das execucoes.
- Persistencia em JSON com leitura inicial e escrita final.
- Testes automatizados com `unittest`.
- Interface principal com `tkinter` e `customtkinter`.

## Como Executar

Na pasta do projeto, execute:

```bash
python -m backupmanager.main
```

A interface principal usa `customtkinter`. Caso nao esteja instalado:

```bash
pip install customtkinter
```

Para abrir a interface visual de preview:

```bash
python preview_interface.py
```

## Testes

Para rodar os testes:

```bash
python -m unittest discover -s tests
```

Para verificar sintaxe dos modulos:

```bash
python -m compileall backupmanager
```

## Estrutura

```text
backupmanager/        Codigo principal do sistema
tests/                Testes automatizados
data/                 Arquivos locais de configuracao e historico
docs/                 Documentacao do projeto
preview_interface.py  Prototipo visual da interface
```

## Observacao

Os arquivos JSON dentro de `data/` sao dados locais de uso da aplicacao e nao sao versionados.
