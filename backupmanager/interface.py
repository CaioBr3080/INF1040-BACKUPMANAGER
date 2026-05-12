"""Interface grafica do BackupManager usando tkinter e funcoes."""

import tkinter as tk
from tkinter import messagebox

from backupmanager import controller
from backupmanager.return_codes import obter_mensagem


def iniciar_interface():
    """Inicia a interface grafica."""
    controller.inicializar_aplicacao()
    estado_interface = criar_estado_interface()
    janela = criar_janela_principal()
    estado_interface["janela"] = janela
    criar_area_perfis(janela, estado_interface)
    criar_area_origens_destinos(janela, estado_interface)
    criar_area_restricoes(janela, estado_interface)
    janela.mainloop()


def criar_estado_interface():
    """Cria o dicionario de estado da interface."""
    return {
        "janela": None,
        "lista_perfis": None,
        "entrada_nome": None,
        "lista_origens": None,
        "lista_destinos": None,
        "entrada_extensoes": None,
        "entrada_nome_contem": None,
        "entrada_tamanho_min": None,
        "entrada_tamanho_max": None,
        "perfil_selecionado_id": None,
    }


def criar_janela_principal():
    """Cria a janela principal."""
    janela = tk.Tk()
    janela.title("BackupManager")
    janela.geometry("900x600")
    return janela


def criar_area_perfis(janela, estado_interface):
    """Cria a area de perfis."""
    frame = tk.LabelFrame(janela, text="Perfis")
    frame.pack(fill="x", padx=8, pady=8)
    estado_interface["lista_perfis"] = tk.Listbox(frame, height=6)
    estado_interface["lista_perfis"].pack(fill="x", padx=8, pady=8)
    return frame


def criar_area_origens_destinos(janela, estado_interface):
    """Cria a area de origens e destinos."""
    frame = tk.LabelFrame(janela, text="Origens e destinos")
    frame.pack(fill="both", expand=True, side="left", padx=8, pady=8)
    estado_interface["lista_origens"] = tk.Listbox(frame)
    estado_interface["lista_origens"].pack(fill="both", expand=True, padx=8, pady=8)
    estado_interface["lista_destinos"] = tk.Listbox(frame)
    estado_interface["lista_destinos"].pack(fill="both", expand=True, padx=8, pady=8)
    return frame


def criar_area_restricoes(janela, estado_interface):
    """Cria a area de restricoes e agendamento."""
    frame = tk.LabelFrame(janela, text="Restricoes e agendamento")
    frame.pack(fill="both", expand=True, side="right", padx=8, pady=8)
    estado_interface["entrada_extensoes"] = tk.Entry(frame)
    estado_interface["entrada_extensoes"].pack(fill="x", padx=8, pady=8)
    estado_interface["entrada_nome_contem"] = tk.Entry(frame)
    estado_interface["entrada_nome_contem"].pack(fill="x", padx=8, pady=8)
    return frame


def atualizar_lista_perfis(estado_interface):
    """Atualiza a lista visual de perfis."""
    codigo, perfis = controller.obter_perfis()
    if codigo != 0:
        mostrar_mensagem_resultado(codigo)
        return codigo

    lista = estado_interface["lista_perfis"]
    lista.delete(0, tk.END)
    for perfil in perfis:
        lista.insert(tk.END, perfil.get("nome", "Sem nome"))
    return codigo


def obter_dados_formulario(estado_interface):
    """Coleta dados basicos do formulario."""
    return {
        "nome": estado_interface["entrada_nome"].get()
        if estado_interface.get("entrada_nome")
        else "",
        "perfil_selecionado_id": estado_interface.get("perfil_selecionado_id"),
    }


def preencher_formulario_com_perfil(estado_interface, perfil):
    """Preenche campos da interface com dados do perfil."""
    estado_interface["perfil_selecionado_id"] = perfil.get("id")
    return perfil


def mostrar_mensagem_resultado(codigo):
    """Exibe mensagem correspondente a um codigo de retorno."""
    mensagem = obter_mensagem(codigo)
    if codigo == 0:
        messagebox.showinfo("BackupManager", mensagem)
    else:
        messagebox.showerror("BackupManager", mensagem)

