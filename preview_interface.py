"""Preview visual da tela inicial do BackupManager.

Este arquivo e independente dos modulos principais do projeto.
Ele usa dados simulados e customtkinter apenas para prototipacao visual.
"""

import tkinter as tk
from tkinter import ttk

try:
    import customtkinter as ctk
except ModuleNotFoundError as erro:
    raise SystemExit(
        "customtkinter nao esta instalado. Instale com: pip install customtkinter"
    ) from erro


COR_FUNDO = "#0b1120"
COR_CARD = "#111827"
COR_CARD_2 = "#172033"
COR_CAMPO = "#0f172a"
COR_BORDA = "#273449"
COR_TEXTO = "#e5e7eb"
COR_TEXTO_FRACO = "#94a3b8"
COR_AZUL = "#3b82f6"
COR_VERDE = "#10b981"
COR_VERMELHO = "#ef4444"


def criar_estado_mock():
    """Cria o estado simulado da interface."""
    return {
        "janela": None,
        "perfil_selecionado_id": "perfil_001",
        "contador_perfis": 3,
        "perfis": [
            {
                "id": "perfil_001",
                "nome": "Backup Faculdade",
                "ativo": True,
                "operacao": "copiar",
            },
            {
                "id": "perfil_002",
                "nome": "Projetos Python",
                "ativo": True,
                "operacao": "copiar",
            },
            {
                "id": "perfil_003",
                "nome": "Arquivos de Edição",
                "ativo": False,
                "operacao": "mover",
            },
        ],
        "origens": [
            "C:/Users/Caio/Documents/PUC",
            "C:/Users/Caio/Desktop/Trabalhos",
        ],
        "destinos": [
            "D:/Backups/PUC",
            "E:/BackupExtra/PUC",
        ],
        "restricoes": {
            "extensoes_permitidas": ".pdf, .docx, .py",
            "nome_contem": "relatorio",
            "tamanho_min": "0",
            "tamanho_max": "10485760",
            "data_modificacao": "2026-05-11 14:30:00",
        },
        "filtros_nome_tipo": [
            {"nome": "relatorio", "tipo": ".pdf"},
            {"nome": "main", "tipo": ".py"},
            {"nome": "ficha", "tipo": ".docx"},
        ],
        "widgets": {},
    }


def configurar_estilo():
    """Configura aparencia do customtkinter e do Treeview."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure(
        "Treeview",
        background=COR_CAMPO,
        fieldbackground=COR_CAMPO,
        foreground=COR_TEXTO,
        bordercolor=COR_BORDA,
        rowheight=34,
        font=("Segoe UI", 10),
    )
    estilo.configure(
        "Treeview.Heading",
        background=COR_CARD_2,
        foreground=COR_TEXTO,
        bordercolor=COR_BORDA,
        font=("Segoe UI", 9, "bold"),
    )
    estilo.map(
        "Treeview",
        background=[("selected", "#1d4ed8")],
        foreground=[("selected", "#ffffff")],
    )


def criar_janela():
    """Cria a janela principal da preview."""
    janela = ctk.CTk()
    janela.title("BackupManager - Preview da Interface")
    janela.geometry("1240x760")
    janela.minsize(1120, 700)
    janela.configure(fg_color=COR_FUNDO)
    return janela


def criar_card(container, titulo, subtitulo=None):
    """Cria um bloco visual com titulo."""
    frame = ctk.CTkFrame(
        container,
        fg_color=COR_CARD,
        border_color=COR_BORDA,
        border_width=1,
        corner_radius=8,
    )

    cabecalho = ctk.CTkFrame(frame, fg_color="transparent")
    cabecalho.pack(fill="x", padx=14, pady=(12, 8))

    ctk.CTkLabel(
        cabecalho,
        text=titulo,
        font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
        text_color=COR_TEXTO,
    ).pack(anchor="w")

    if subtitulo:
        ctk.CTkLabel(
            cabecalho,
            text=subtitulo,
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=COR_TEXTO_FRACO,
        ).pack(anchor="w", pady=(2, 0))

    corpo = ctk.CTkFrame(frame, fg_color="transparent")
    corpo.pack(fill="both", expand=True, padx=14, pady=(0, 14))
    corpo.columnconfigure(0, weight=1)
    return frame, corpo


def criar_cabecalho(container):
    """Cria o cabecalho da aplicacao."""
    frame = ctk.CTkFrame(container, fg_color="transparent")
    frame.pack(fill="x", pady=(0, 12))
    frame.columnconfigure(0, weight=1)

    ctk.CTkLabel(
        frame,
        text="BackupManager",
        font=ctk.CTkFont(family="Segoe UI", size=30, weight="bold"),
        text_color=COR_TEXTO,
    ).grid(row=0, column=0, sticky="w")

    ctk.CTkLabel(
        frame,
        text="Preview visual em tema escuro com dados simulados",
        font=ctk.CTkFont(family="Segoe UI", size=13),
        text_color=COR_TEXTO_FRACO,
    ).grid(row=1, column=0, sticky="w", pady=(2, 0))

    ctk.CTkLabel(
        frame,
        text="Prototipo academico",
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        text_color="#bfdbfe",
        fg_color="#1e3a8a",
        corner_radius=16,
        padx=14,
        pady=6,
    ).grid(row=0, column=1, rowspan=2, sticky="e")


def criar_barra_abas(container):
    """Mostra que as tres areas podem virar abas separadas."""
    barra = ctk.CTkFrame(
        container,
        fg_color=COR_CARD,
        border_color=COR_BORDA,
        border_width=1,
        corner_radius=8,
    )
    barra.pack(fill="x", pady=(0, 12))

    textos = ["1  Perfis", "2  Origens e destinos", "3  Restricoes"]
    for indice, texto in enumerate(textos):
        cor = COR_AZUL if indice == 0 else COR_CARD_2
        item = ctk.CTkLabel(
            barra,
            text=texto,
            height=34,
            fg_color=cor,
            text_color=COR_TEXTO,
            corner_radius=6,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        )
        item.pack(side="left", fill="x", expand=True, padx=(10 if indice == 0 else 4, 4), pady=10)


def atualizar_tabela_perfis(estado):
    """Recarrega a tabela de perfis simulados."""
    tabela = estado["widgets"]["tabela_perfis"]
    for item in tabela.get_children():
        tabela.delete(item)

    for perfil in estado["perfis"]:
        status = "Ativo" if perfil["ativo"] else "Inativo"
        tabela.insert(
            "",
            "end",
            iid=perfil["id"],
            values=(perfil["nome"], status, perfil["operacao"]),
        )

    if estado["perfis"]:
        selecionado = estado.get("perfil_selecionado_id") or estado["perfis"][0]["id"]
        if selecionado not in tabela.get_children():
            selecionado = estado["perfis"][0]["id"]
        estado["perfil_selecionado_id"] = selecionado
        tabela.selection_set(selecionado)
        tabela.focus(selecionado)


def adicionar_perfil_mock(estado):
    """Adiciona um perfil apenas na preview."""
    entrada = estado["widgets"]["entrada_novo_perfil"]
    nome = entrada.get().strip()
    if not nome:
        estado["contador_perfis"] += 1
        nome = "Novo Perfil " + str(estado["contador_perfis"])

    estado["contador_perfis"] += 1
    perfil_id = "perfil_" + str(estado["contador_perfis"]).zfill(3)
    estado["perfis"].append(
        {
            "id": perfil_id,
            "nome": nome,
            "ativo": True,
            "operacao": "copiar",
        }
    )
    estado["perfil_selecionado_id"] = perfil_id
    entrada.delete(0, tk.END)
    atualizar_tabela_perfis(estado)


def excluir_perfil_mock(estado):
    """Remove o perfil selecionado apenas na preview."""
    tabela = estado["widgets"]["tabela_perfis"]
    selecao = tabela.selection()
    if not selecao:
        return

    perfil_id = selecao[0]
    estado["perfis"] = [perfil for perfil in estado["perfis"] if perfil["id"] != perfil_id]
    estado["perfil_selecionado_id"] = estado["perfis"][0]["id"] if estado["perfis"] else None
    atualizar_tabela_perfis(estado)


def criar_area_perfis(container, estado):
    """Cria a area lateral de perfis."""
    frame, corpo = criar_card(
        container,
        "Perfis de backup",
        "Adicione, selecione ou remova perfis simulados",
    )
    frame.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
    corpo.rowconfigure(2, weight=1)

    entrada_linha = ctk.CTkFrame(corpo, fg_color="transparent")
    entrada_linha.grid(row=0, column=0, sticky="ew", pady=(0, 8))
    entrada_linha.columnconfigure(0, weight=1)

    entrada = ctk.CTkEntry(
        entrada_linha,
        height=34,
        corner_radius=6,
        placeholder_text="Nome do novo perfil",
    )
    entrada.grid(row=0, column=0, sticky="ew", padx=(0, 8))

    botao_add = ctk.CTkButton(
        entrada_linha,
        text="Adicionar",
        width=92,
        height=34,
        fg_color=COR_AZUL,
        hover_color="#2563eb",
        command=lambda: adicionar_perfil_mock(estado),
    )
    botao_add.grid(row=0, column=1)

    ctk.CTkLabel(
        corpo,
        text="Perfil selecionado",
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        text_color=COR_TEXTO_FRACO,
    ).grid(row=1, column=0, sticky="w", pady=(0, 6))

    colunas = ("nome", "status", "operacao")
    tabela = ttk.Treeview(corpo, columns=colunas, show="headings", height=10)
    tabela.heading("nome", text="Nome")
    tabela.heading("status", text="Status")
    tabela.heading("operacao", text="Operacao")
    tabela.column("nome", width=170, anchor="w")
    tabela.column("status", width=74, anchor="center")
    tabela.column("operacao", width=82, anchor="center")
    tabela.grid(row=2, column=0, sticky="nsew")

    rodape = ctk.CTkFrame(corpo, fg_color="transparent")
    rodape.grid(row=3, column=0, sticky="ew", pady=(12, 0))
    rodape.columnconfigure(0, weight=1)

    ativo = ctk.CTkCheckBox(
        rodape,
        text="Perfil ativo",
        checkbox_width=18,
        checkbox_height=18,
        text_color=COR_TEXTO,
    )
    ativo.select()
    ativo.grid(row=0, column=0, sticky="w")

    ctk.CTkButton(
        rodape,
        text="Excluir selecionado",
        width=138,
        height=32,
        fg_color=COR_VERMELHO,
        hover_color="#dc2626",
        command=lambda: excluir_perfil_mock(estado),
    ).grid(row=0, column=1, sticky="e")

    estado["widgets"]["entrada_novo_perfil"] = entrada
    estado["widgets"]["tabela_perfis"] = tabela
    estado["widgets"]["check_ativo"] = ativo
    atualizar_tabela_perfis(estado)
    return frame


def criar_lista_visual(container, titulo, itens):
    """Cria uma lista visual simulada com botoes."""
    bloco = ctk.CTkFrame(container, fg_color=COR_CARD_2, corner_radius=8)
    bloco.columnconfigure(0, weight=1)

    ctk.CTkLabel(
        bloco,
        text=titulo,
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        text_color=COR_TEXTO,
    ).grid(row=0, column=0, sticky="w", padx=10, pady=(10, 6))

    lista = tk.Listbox(
        bloco,
        height=5,
        relief="flat",
        bd=0,
        activestyle="none",
        font=("Segoe UI", 10),
        bg=COR_CAMPO,
        fg=COR_TEXTO,
        selectbackground="#1d4ed8",
        selectforeground="#ffffff",
        highlightthickness=1,
        highlightbackground=COR_BORDA,
        exportselection=False,
    )
    lista.grid(row=1, column=0, sticky="nsew", padx=10)

    for item in itens:
        lista.insert(tk.END, item)

    botoes = ctk.CTkFrame(bloco, fg_color="transparent")
    botoes.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
    ctk.CTkButton(botoes, text="Adicionar", height=30, width=92).pack(side="left")
    ctk.CTkButton(
        botoes,
        text="Remover",
        height=30,
        width=86,
        fg_color="#334155",
        hover_color="#475569",
        text_color=COR_TEXTO,
    ).pack(side="left", padx=(8, 0))

    return bloco, lista


def criar_area_origens_destinos(container, estado):
    """Cria a area central de origens, destinos e operacao."""
    frame, corpo = criar_card(
        container,
        "Origens e destinos",
        "Pastas envolvidas na rotina de backup",
    )
    frame.grid(row=0, column=2, sticky="nsew", padx=8)
    corpo.rowconfigure(0, weight=1)
    corpo.rowconfigure(1, weight=1)

    bloco_origens, lista_origens = criar_lista_visual(
        corpo,
        "Pastas de origem",
        estado["origens"],
    )
    bloco_origens.grid(row=0, column=0, sticky="nsew", pady=(0, 10))

    bloco_destinos, lista_destinos = criar_lista_visual(
        corpo,
        "Pastas de destino",
        estado["destinos"],
    )
    bloco_destinos.grid(row=1, column=0, sticky="nsew", pady=(0, 10))

    operacao_frame = ctk.CTkFrame(corpo, fg_color=COR_CARD_2, corner_radius=8)
    operacao_frame.grid(row=2, column=0, sticky="ew")

    ctk.CTkLabel(
        operacao_frame,
        text="Operacao",
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        text_color=COR_TEXTO,
    ).pack(anchor="w", padx=10, pady=(10, 4))

    operacao_var = tk.StringVar(value="copiar")
    opcoes = ctk.CTkFrame(operacao_frame, fg_color="transparent")
    opcoes.pack(fill="x", padx=10, pady=(0, 10))
    ctk.CTkRadioButton(
        opcoes,
        text="Copiar",
        variable=operacao_var,
        value="copiar",
        text_color=COR_TEXTO,
    ).pack(side="left")
    ctk.CTkRadioButton(
        opcoes,
        text="Mover",
        variable=operacao_var,
        value="mover",
        text_color=COR_TEXTO,
    ).pack(side="left", padx=(18, 0))

    estado["widgets"]["lista_origens"] = lista_origens
    estado["widgets"]["lista_destinos"] = lista_destinos
    estado["widgets"]["operacao_var"] = operacao_var
    return frame


def criar_campo(container, texto, valor):
    """Cria um campo preenchido com valor simulado."""
    ctk.CTkLabel(
        container,
        text=texto,
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        text_color=COR_TEXTO,
    ).pack(anchor="w", pady=(0, 4))

    entrada = ctk.CTkEntry(
        container,
        height=34,
        corner_radius=6,
        fg_color=COR_CAMPO,
        border_color=COR_BORDA,
        text_color=COR_TEXTO,
    )
    entrada.insert(0, valor)
    entrada.pack(fill="x", pady=(0, 10))
    return entrada


def atualizar_lista_filtros(estado):
    """Atualiza a lista visual de filtros nome + tipo."""
    lista = estado["widgets"]["lista_filtros_nome_tipo"]
    lista.delete(0, tk.END)
    for filtro in estado["filtros_nome_tipo"]:
        lista.insert(tk.END, filtro["nome"] + "  |  " + filtro["tipo"])


def adicionar_filtro_nome_tipo(estado):
    """Adiciona uma regra visual de nome e tipo de arquivo."""
    entrada_nome = estado["widgets"]["entrada_filtro_nome"]
    entrada_tipo = estado["widgets"]["entrada_filtro_tipo"]
    nome = entrada_nome.get().strip()
    tipo = entrada_tipo.get().strip()

    if not nome and not tipo:
        return
    if not nome:
        nome = "*"
    if not tipo:
        tipo = "*"
    if tipo != "*" and not tipo.startswith("."):
        tipo = "." + tipo

    estado["filtros_nome_tipo"].append({"nome": nome, "tipo": tipo})
    entrada_nome.delete(0, tk.END)
    entrada_tipo.delete(0, tk.END)
    atualizar_lista_filtros(estado)


def remover_filtro_nome_tipo(estado):
    """Remove a regra visual selecionada."""
    lista = estado["widgets"]["lista_filtros_nome_tipo"]
    selecao = lista.curselection()
    if not selecao:
        return
    indice = selecao[0]
    del estado["filtros_nome_tipo"][indice]
    atualizar_lista_filtros(estado)


def criar_area_filtros_nome_tipo(container, estado):
    """Cria a area para varios nomes e tipos de arquivo."""
    bloco = ctk.CTkFrame(container, fg_color=COR_CARD_2, corner_radius=8)
    bloco.pack(fill="x", pady=(2, 10))
    bloco.columnconfigure(0, weight=1)

    ctk.CTkLabel(
        bloco,
        text="Arquivos especificos no perfil",
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        text_color=COR_TEXTO,
    ).grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=(10, 6))

    entrada_nome = ctk.CTkEntry(
        bloco,
        height=32,
        placeholder_text="Nome",
        fg_color=COR_CAMPO,
        border_color=COR_BORDA,
    )
    entrada_nome.grid(row=1, column=0, sticky="ew", padx=(10, 6))

    entrada_tipo = ctk.CTkEntry(
        bloco,
        height=32,
        width=82,
        placeholder_text=".tipo",
        fg_color=COR_CAMPO,
        border_color=COR_BORDA,
    )
    entrada_tipo.grid(row=1, column=1, sticky="ew", padx=(0, 6))

    ctk.CTkButton(
        bloco,
        text="Adicionar",
        width=88,
        height=32,
        command=lambda: adicionar_filtro_nome_tipo(estado),
    ).grid(row=1, column=2, sticky="e", padx=(0, 10))

    lista = tk.Listbox(
        bloco,
        height=4,
        relief="flat",
        bd=0,
        activestyle="none",
        font=("Segoe UI", 10),
        bg=COR_CAMPO,
        fg=COR_TEXTO,
        selectbackground="#1d4ed8",
        selectforeground="#ffffff",
        highlightthickness=1,
        highlightbackground=COR_BORDA,
        exportselection=False,
    )
    lista.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=(8, 8))

    ctk.CTkButton(
        bloco,
        text="Remover regra selecionada",
        height=30,
        fg_color="#334155",
        hover_color="#475569",
        command=lambda: remover_filtro_nome_tipo(estado),
    ).grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 10))

    estado["widgets"]["entrada_filtro_nome"] = entrada_nome
    estado["widgets"]["entrada_filtro_tipo"] = entrada_tipo
    estado["widgets"]["lista_filtros_nome_tipo"] = lista
    atualizar_lista_filtros(estado)


def criar_area_restricoes(container, estado):
    """Cria a area direita de restricoes e agendamento."""
    frame, corpo = criar_card(
        container,
        "Restricoes e agendamento",
        "Filtros, nomes especificos e forma de execucao",
    )
    frame.grid(row=0, column=4, sticky="nsew", padx=(8, 0))

    restricoes = estado["restricoes"]
    estado["widgets"]["entrada_extensoes"] = criar_campo(
        corpo,
        "Extensoes permitidas",
        restricoes["extensoes_permitidas"],
    )
    estado["widgets"]["entrada_nome_contem"] = criar_campo(
        corpo,
        "Nome contem",
        restricoes["nome_contem"],
    )

    criar_area_filtros_nome_tipo(corpo, estado)

    estado["widgets"]["entrada_tamanho_min"] = criar_campo(
        corpo,
        "Tamanho minimo (bytes)",
        restricoes["tamanho_min"],
    )
    estado["widgets"]["entrada_tamanho_max"] = criar_campo(
        corpo,
        "Tamanho maximo (bytes)",
        restricoes["tamanho_max"],
    )
    estado["widgets"]["entrada_data_modificacao"] = criar_campo(
        corpo,
        "Data de modificacao",
        restricoes["data_modificacao"],
    )

    agendamento_frame = ctk.CTkFrame(corpo, fg_color=COR_CARD_2, corner_radius=8)
    agendamento_frame.pack(fill="x", pady=(4, 0))

    ctk.CTkLabel(
        agendamento_frame,
        text="Agendamento",
        font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
        text_color=COR_TEXTO,
    ).pack(anchor="w", padx=10, pady=(10, 6))

    agendamento_var = tk.StringVar(value="manual")
    ctk.CTkRadioButton(
        agendamento_frame,
        text="Manual",
        variable=agendamento_var,
        value="manual",
        text_color=COR_TEXTO,
    ).pack(anchor="w", padx=10, pady=3)
    ctk.CTkRadioButton(
        agendamento_frame,
        text="Intervalo",
        variable=agendamento_var,
        value="intervalo",
        text_color=COR_TEXTO,
    ).pack(anchor="w", padx=10, pady=3)
    ctk.CTkRadioButton(
        agendamento_frame,
        text="Alteracao",
        variable=agendamento_var,
        value="alteracao",
        text_color=COR_TEXTO,
    ).pack(anchor="w", padx=10, pady=3)

    intervalo_linha = ctk.CTkFrame(agendamento_frame, fg_color="transparent")
    intervalo_linha.pack(fill="x", padx=10, pady=(8, 10))
    intervalo_linha.columnconfigure(0, weight=1)

    entrada_intervalo = ctk.CTkEntry(
        intervalo_linha,
        height=32,
        corner_radius=6,
        placeholder_text="Intervalo",
        fg_color=COR_CAMPO,
        border_color=COR_BORDA,
    )
    entrada_intervalo.insert(0, "30")
    entrada_intervalo.grid(row=0, column=0, sticky="ew", padx=(0, 8))

    seletor_unidade = ctk.CTkOptionMenu(
        intervalo_linha,
        height=32,
        width=112,
        values=["segundos", "minutos", "horas"],
        fg_color=COR_CAMPO,
        button_color="#334155",
        button_hover_color="#475569",
        dropdown_fg_color=COR_CARD,
        dropdown_hover_color="#1d4ed8",
        text_color=COR_TEXTO,
    )
    seletor_unidade.set("minutos")
    seletor_unidade.grid(row=0, column=1, sticky="e")

    estado["widgets"]["agendamento_var"] = agendamento_var
    estado["widgets"]["entrada_intervalo"] = entrada_intervalo
    estado["widgets"]["seletor_unidade_intervalo"] = seletor_unidade
    return frame


def criar_barra_botoes(container, janela, estado):
    """Cria a barra inferior de acoes simuladas."""
    frame = ctk.CTkFrame(
        container,
        fg_color=COR_CARD,
        border_color=COR_BORDA,
        border_width=1,
        corner_radius=8,
    )
    frame.pack(fill="x", pady=(14, 0))

    botoes = [
        ("Criar Perfil", COR_AZUL, "#2563eb", lambda: adicionar_perfil_mock(estado)),
        ("Salvar Perfil", "#0f766e", "#0d9488", None),
        ("Executar Backup", COR_VERDE, "#059669", None),
        ("Ver Historico", "#475569", "#334155", None),
        ("Sair", "#e5e7eb", "#d1d5db", janela.destroy),
    ]

    for texto, cor, hover, comando in botoes:
        texto_cor = "#111827" if texto == "Sair" else "#ffffff"
        ctk.CTkButton(
            frame,
            text=texto,
            height=38,
            fg_color=cor,
            hover_color=hover,
            text_color=texto_cor,
            command=comando,
        ).pack(side="left", padx=(12, 0), pady=12)


def criar_separador(container, coluna):
    """Cria uma barra fina entre as areas principais."""
    barra = ctk.CTkFrame(container, fg_color="#334155", width=3, corner_radius=3)
    barra.grid(row=0, column=coluna, sticky="ns", padx=4)
    return barra


def criar_conteudo_principal(container, estado):
    """Organiza as tres areas principais da tela."""
    frame = ctk.CTkFrame(container, fg_color="transparent")
    frame.pack(fill="both", expand=True)
    frame.columnconfigure(0, weight=1, uniform="areas")
    frame.columnconfigure(1, weight=0)
    frame.columnconfigure(2, weight=1, uniform="areas")
    frame.columnconfigure(3, weight=0)
    frame.columnconfigure(4, weight=1, uniform="areas")
    frame.rowconfigure(0, weight=1)

    criar_area_perfis(frame, estado)
    criar_separador(frame, 1)
    criar_area_origens_destinos(frame, estado)
    criar_separador(frame, 3)
    criar_area_restricoes(frame, estado)


def iniciar_preview():
    """Inicia a preview visual da interface."""
    estado = criar_estado_mock()
    configurar_estilo()

    janela = criar_janela()
    estado["janela"] = janela

    container = ctk.CTkFrame(janela, fg_color="transparent")
    container.pack(fill="both", expand=True, padx=18, pady=18)

    criar_cabecalho(container)
    criar_barra_abas(container)
    criar_conteudo_principal(container, estado)
    criar_barra_botoes(container, janela, estado)

    janela.mainloop()


if __name__ == "__main__":
    iniciar_preview()
