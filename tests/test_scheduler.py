import unittest

from backupmanager import scheduler
from backupmanager.return_codes import OK


class TestScheduler(unittest.TestCase):
    def test_comparar_estado_arquivos(self):
        self.assertTrue(scheduler.comparar_estado_arquivos({"a": 1}, {"a": 2}))
        self.assertFalse(scheduler.comparar_estado_arquivos({"a": 1}, {"a": 1}))

    def test_parar_monitoramento(self):
        codigo = scheduler.parar_monitoramento()

        self.assertEqual(codigo, OK)


if __name__ == "__main__":
    unittest.main()

