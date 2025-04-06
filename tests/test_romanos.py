import unittest
from src.convertir_romano import convertir_a_romano 




class PruebasConversionRomana(unittest.TestCase):

    def test_numeros_unidades(self):
        self.assertEqual(convertir_a_romano(1), "I")
        self.assertEqual(convertir_a_romano(5), "V")
        self.assertEqual(convertir_a_romano(8), "VIII")

if __name__ == '__main__':

    unittest.main()