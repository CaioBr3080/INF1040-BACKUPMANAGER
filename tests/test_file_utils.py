import unittest

from backupmanager import file_utils


class TestFileUtils(unittest.TestCase):
    def test_filtrar_por_extensao(self):
        arquivo = {"extensao": ".py", "nome": "main.py", "tamanho": 10}
        restricoes = {"extensoes_permitidas": [".py"]}

        self.assertTrue(file_utils.atende_restricao_extensao(arquivo, restricoes))

    def test_filtrar_por_nome(self):
        arquivo = {"extensao": ".txt", "nome": "relatorio_final.txt", "tamanho": 10}
        restricoes = {"nome_contem": "relatorio"}

        self.assertTrue(file_utils.atende_restricao_nome(arquivo, restricoes))

    def test_filtrar_por_tamanho_minimo(self):
        arquivo = {"extensao": ".txt", "nome": "a.txt", "tamanho": 100}
        restricoes = {"tamanho_min": 50, "tamanho_max": None}

        self.assertTrue(file_utils.atende_restricao_tamanho(arquivo, restricoes))


if __name__ == "__main__":
    unittest.main()

