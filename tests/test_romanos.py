import unittest
from src.convertir_romano import convertir_a_romano 


class PruebasConversionRomana(unittest.TestCase):

    def test_numeros_unidades(self):
        self.assertEqual(convertir_a_romano(1), "I")
        self.assertEqual(convertir_a_romano(5), "V")
        self.assertEqual(convertir_a_romano(8), "VIII")

    def test_numeros_unidades(self):
        self.asserEqual(convertir_a_romano(9), "IX")
        self.assertEqual(convertir_a_romano(40), "XL")
        self.assertEqual(convertir_a_romano(90), "XC")
        self.assertEqual(convertir_a_romano(400), "CD")
        self.assertEqual(convertir_a_romano(900), "CM")

    def test_valores_complejos(self):
        self.assertEqual(convertir_a_romano(1987), "MCMLXXXVII")
        self.assertEqual(convertir_a_romano(2421), "MMCDXXI")
        self.assertEqual(convertir_a_romano(3210), "MMMCCX")
        self.assertEqual(convertir_a_romano(3999), "MMMCMXCIX")
    
if __name__ == '__main__':

    unittest.main()