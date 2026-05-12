import unittest

from backupmanager import backup_engine
from backupmanager.return_codes import ERRO_BACKUP_SEM_ARQUIVOS


class TestBackupEngine(unittest.TestCase):
    def test_montar_resultado_backup(self):
        resultado = backup_engine.montar_resultado_backup("perfil_001")

        self.assertEqual(resultado["perfil_id"], "perfil_001")
        self.assertEqual(resultado["arquivos_processados"], 0)

    def test_executar_backup_base_sem_arquivos(self):
        codigo, resultado = backup_engine.executar_backup({"id": "perfil_001"})

        self.assertEqual(codigo, ERRO_BACKUP_SEM_ARQUIVOS)
        self.assertEqual(resultado["perfil_id"], "perfil_001")


if __name__ == "__main__":
    unittest.main()

