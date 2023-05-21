import unittest
from src.novo import soma


class testsoma(unittest.TestCase):
    def test_retorno_soma(self):
        self.assertEqual(soma(10, 10), 20)

    def teste_retorno_soma_10_20(self):
        self.assertEqual(soma(10, 20), 30)
