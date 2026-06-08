# Especificação Atualizada — BackupManager

Este documento consolida as regras atuais do projeto BackupManager para a disciplina INF1040.

## Objetivo

O BackupManager é uma aplicação desktop local para gerenciar perfis de backup. Cada perfil define:

- nome;
- origens;
- destinos;
- operação de copiar ou mover;
- restrições de arquivos;
- agendamento;
- estado ativo/inativo;
- histórico de execuções.

## Regras Principais

- Usar Python.
- Usar dicionários para representar entidades.
- Não usar classes na lógica principal.
- Não usar dataclasses.
- Manter o projeto modular.
- Usar códigos de retorno padronizados.
- Usar testes automatizados com `unittest`.
- Usar JSON para persistência local.
- Usar `customtkinter` apenas para aparência da interface.

## Persistência em Memória

A regra atual de persistência é:

```text
JSON -> leitura inicial -> ESTADO em memória -> alterações em memória -> escrita final no encerramento
```

Durante a execução normal, operações como criar perfil, editar perfil, excluir perfil, executar backup e registrar histórico não devem salvar JSON imediatamente.

O `controller.py` mantém o estado central:

```python
ESTADO = {
    "perfis": [],
    "historico": [],
    "config": {},
    "alterado": False
}
```

Quando houver alteração em perfis, histórico ou configuração:

```python
ESTADO["alterado"] = True
```

Os JSONs só devem ser reescritos em:

```python
controller.finalizar_aplicacao()
```

## Arquitetura

```text
Usuário
  ↓
interface.py
  ↓
controller.py
  ├── perfil_manager.py
  ├── backup_engine.py
  │      └── file_utils.py
  ├── scheduler.py
  │      └── file_utils.py
  ├── history_manager.py
  └── storage.py
         └── data/*.json
```

Durante a execução normal:

```text
interface.py -> controller.py -> módulos internos -> ESTADO em memória
```

`storage.py` deve ser usado principalmente na inicialização e finalização.

## Responsabilidade dos Módulos

### `interface.py`

Interface gráfica com `tkinter` e `customtkinter`.

Deve chamar o `controller.py` e não executar regras complexas de backup diretamente.

### `controller.py`

Camada central da aplicação.

Responsável por carregar dados, manter `ESTADO`, coordenar módulos internos e salvar JSON apenas no encerramento.

### `perfil_manager.py`

Criação, consulta, edição, ativação, desativação e exclusão de perfis em memória.

### `file_utils.py`

Funções auxiliares de sistema de arquivos: listar arquivos, obter metadados, verificar caminhos e aplicar filtros.

### `backup_engine.py`

Execução real do backup: copiar, mover, múltiplos destinos, restrições e resultado da execução.

### `history_manager.py`

Criação e consulta de registros de histórico em memória.

### `scheduler.py`

Execução automática simples por intervalo ou alteração.

### `storage.py`

Leitura e escrita de JSON.

### `return_codes.py`

Códigos de retorno e mensagens padronizadas.

## Ordem Recomendada de Implementação

1. Finalizar `file_utils.py`.
2. Implementar backup real em `backup_engine.py`.
3. Reforçar validações no `controller.py`.
4. Melhorar histórico.
5. Implementar scheduler.
6. Refinar interface.
