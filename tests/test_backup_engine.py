import unittest
from pathlib import Path

from backupmanager import backup_engine
from backupmanager.return_codes import (
    OK,
    ERRO_BACKUP_SEM_ARQUIVOS,
    ERRO_DADOS_INVALIDOS,
    ERRO_DESTINO_INVALIDO,
    ERRO_OPERACAO_INVALIDA,
    ERRO_ORIGEM_INVALIDA,
)


class TestBackupEngine(unittest.TestCase):
    def test_montar_resultado_backup(self):
        resultado = backup_engine.montar_resultado_backup("perfil_001")

        self.assertEqual(resultado["perfil_id"], "perfil_001")
        self.assertEqual(resultado["arquivos_processados"], 0)

    def test_executar_backup_base_sem_arquivos(self):
        codigo, resultado = backup_engine.executar_backup({
            "id": "perfil_001",
            "origens": ["C:/origem"],
            "destinos": ["D:/destino"],
            "operacao": "copiar",
        })

        self.assertEqual(codigo, ERRO_BACKUP_SEM_ARQUIVOS)
        self.assertEqual(resultado["perfil_id"], "perfil_001")

    def test_validar_perfil_para_backup_valido(self):
        perfil = {
            "id": "perfil_001",
            "origens": ["C:/origem"],
            "destinos": ["D:/destino"],
            "operacao": "copiar",
        }

        self.assertEqual(backup_engine.validar_perfil_para_backup(perfil), OK)

    def test_validar_perfil_para_backup_rejeita_dados_invalidos(self):
        self.assertEqual(
            backup_engine.validar_perfil_para_backup(None),
            ERRO_DADOS_INVALIDOS,
        )

    def test_validar_perfil_para_backup_rejeita_sem_origem(self):
        perfil = {
            "id": "perfil_001",
            "origens": [],
            "destinos": ["D:/destino"],
            "operacao": "copiar",
        }

        self.assertEqual(
            backup_engine.validar_perfil_para_backup(perfil),
            ERRO_ORIGEM_INVALIDA,
        )

    def test_validar_perfil_para_backup_rejeita_sem_destino(self):
        perfil = {
            "id": "perfil_001",
            "origens": ["C:/origem"],
            "destinos": [],
            "operacao": "copiar",
        }

        self.assertEqual(
            backup_engine.validar_perfil_para_backup(perfil),
            ERRO_DESTINO_INVALIDO,
        )

    def test_validar_perfil_para_backup_rejeita_operacao_invalida(self):
        perfil = {
            "id": "perfil_001",
            "origens": ["C:/origem"],
            "destinos": ["D:/destino"],
            "operacao": "compactar",
        }

        self.assertEqual(
            backup_engine.validar_perfil_para_backup(perfil),
            ERRO_OPERACAO_INVALIDA,
        )

    def test_executar_backup_retorna_erro_de_validacao(self):
        codigo, resultado = backup_engine.executar_backup({
            "id": "perfil_001",
            "origens": [],
            "destinos": ["D:/destino"],
            "operacao": "copiar",
        })

        self.assertEqual(codigo, ERRO_ORIGEM_INVALIDA)
        self.assertEqual(resultado["status"], "erro")
        self.assertEqual(resultado["perfil_id"], "perfil_001")
        self.assertTrue(resultado["erros"])

    def test_gerar_caminho_destino_com_nome(self):
        arquivo = {"nome": "relatorio.txt", "caminho": "C:/origem/relatorio.txt"}

        caminho = backup_engine.gerar_caminho_destino(arquivo, "D:/backup")

        self.assertEqual(caminho, str(Path("D:/backup") / "relatorio.txt"))

    def test_gerar_caminho_destino_com_caminho_sem_nome(self):
        arquivo = {"caminho": "C:/origem/relatorio.txt"}

        caminho = backup_engine.gerar_caminho_destino(arquivo, "D:/backup")

        self.assertEqual(caminho, str(Path("D:/backup") / "relatorio.txt"))

    def test_gerar_caminho_destino_rejeita_dados_invalidos(self):
        self.assertIsNone(backup_engine.gerar_caminho_destino(None, "D:/backup"))
        self.assertIsNone(backup_engine.gerar_caminho_destino({}, "D:/backup"))
        self.assertIsNone(backup_engine.gerar_caminho_destino({"nome": "a.txt"}, ""))


if __name__ == "__main__":
    unittest.main()
