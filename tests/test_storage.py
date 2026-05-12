import tempfile
import unittest
from pathlib import Path

from backupmanager import storage
from backupmanager.return_codes import OK, ERRO_JSON_CORROMPIDO


class TestStorage(unittest.TestCase):
    def test_salvar_e_carregar_json(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "dados.json"
            dados = [{"nome": "Backup"}]

            codigo_salvar = storage.salvar_json(caminho, dados)
            codigo_carregar, carregado = storage.carregar_json(caminho, [])

            self.assertEqual(codigo_salvar, OK)
            self.assertEqual(codigo_carregar, OK)
            self.assertEqual(carregado, dados)

    def test_carregar_json_inexistente(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "inexistente.json"

            codigo, carregado = storage.carregar_json(caminho, [])

            self.assertEqual(codigo, OK)
            self.assertEqual(carregado, [])

    def test_carregar_json_corrompido(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "dados.json"
            caminho.write_text("{json invalido", encoding="utf-8")

            codigo, carregado = storage.carregar_json(caminho, [])

            self.assertEqual(codigo, ERRO_JSON_CORROMPIDO)
            self.assertEqual(carregado, [])


if __name__ == "__main__":
    unittest.main()

