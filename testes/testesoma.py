import unittest
from src.novo import soma, fatorial

class testsoma(unittest.TestCase):
    def test_retorno_soma(self):
        self.assertEqual(soma(10, 10), 20)

    def teste_retorno_soma_10_20(self):
        self.assertEqual(soma(10, 20), 30)
    
    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)       

    def test_fatorial1(self):
        self.assertEqual(fatorial(3), 6)      

