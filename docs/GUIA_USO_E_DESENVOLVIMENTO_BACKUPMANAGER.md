# Guia de Uso e Desenvolvimento — BackupManager

## Como Executar

Na pasta do projeto:

```bash
python -m backupmanager.main
```

A interface usa `customtkinter`. Se necessário:

```bash
pip install customtkinter
```

## Como Rodar Testes

```bash
python -m unittest discover -s tests
```

Para verificar sintaxe:

```bash
python -m compileall backupmanager
```

## Uso Básico da Interface

### Criar Perfil

Digite um nome e clique em `Criar perfil`.

### Selecionar Perfil

Clique em um perfil na lista. Os dados aparecem no formulário.

### Editar Perfil

Altere nome, ativo/inativo, origens, destinos, operação, restrições ou agendamento e clique em `Aplicar alteracoes`.

Esse botão altera apenas o estado em memória.

### Adicionar Origem ou Destino

Use `Adicionar origem` ou `Adicionar destino`, escolha uma pasta e depois clique em `Aplicar alteracoes`.

### Executar Backup

Selecione um perfil e clique em `Executar backup`.

### Ver Histórico

Selecione um perfil e clique em `Historico`.

### Sair

Ao clicar em `Sair` ou fechar a janela, a aplicação chama `controller.finalizar_aplicacao()`.

Se houver alterações, os JSONs são reescritos nesse momento.

## Próximos Módulos a Fazer

### `file_utils.py`

É o próximo módulo mais importante.

Espera-se implementar:

- verificar existência de caminhos;
- verificar diretórios;
- listar arquivos;
- obter nome, extensão, tamanho e data de modificação;
- filtrar por extensão;
- filtrar por nome;
- filtrar por tamanho;
- filtrar por data;
- testar com `tempfile`.

### `backup_engine.py`

Depende de `file_utils.py`.

Espera-se implementar:

- backup real de arquivos;
- cópia;
- movimentação;
- múltiplos destinos;
- criação de pasta destino;
- tratamento de erro por arquivo;
- resultado com contadores e erros.

### `controller.py`

Espera-se reforçar:

- validação de perfil ativo;
- validação de origem/destino;
- bloqueio de backup sem origem ou destino;
- funções para limpar histórico;
- mais testes de erro.

### `history_manager.py`

Espera-se melhorar:

- testes de limpeza de histórico;
- padronização de status;
- garantia de que erros sempre sejam lista.

### `scheduler.py`

Espera-se implementar:

- execução por intervalo;
- detecção simples de alteração;
- monitoramento com `threading`;
- callback para o controller;
- respeito a perfil ativo/inativo.

### `interface.py`

Espera-se refinar:

- tela ou janela de histórico;
- campos de data de modificação;
- mensagens de validação mais claras;
- feedback visual após backup.

### `storage.py`

Espera-se reforçar:

- tratamento de erro ao salvar;
- tratamento de permissão;
- criação de arquivos padrão quando necessário.
