import libcomplex as LC
import unittest

class complex_operations(unittest.TestCase):

    def test_sumacomplex(self):
        suma = LC.sumacomplex((4, 5), (6, 7))
        self.assertAlmostEqual(suma[0], 10)
        self.assertAlmostEqual(suma[1], 12)

    def test_restacomplex(self):
        resta = LC.restacomplex((4, 5), (6, 7))
        self.assertAlmostEqual(resta[0], -2)
        self.assertAlmostEqual(resta[1], -2)

    def test_productocomplex(self):
        producto = LC.productocomplex((4, 5), (6, 7))
        self.assertAlmostEqual(producto[0], -11)
        self.assertAlmostEqual(producto[1], 58)

    def test_divisioncomplex(self):
        division = LC.divisioncomplex((4, 5), (6, 7))
        self.assertAlmostEqual(division[0], 0.6941176470588235)
        self.assertAlmostEqual(division[1], 0.023529411764705882)
    
    def test_modulocomplex(self):
        mod = LC.modulocomplex((4,5))
        self.assertAlmostEqual(mod,6.4031242374328485) 

    def test_conjugadocomplex(self):
        conjugado = LC.conjugadocomplex((4,5))
        self.assertAlmostEqual(conjugado[0], 4)
        self.assertAlmostEqual(conjugado[1], -5)
    
    def test_cartesianoa_polarcomplex(self):
        conversion1 = LC.cartesianoa_polarcomplex((4,5))
        self.assertAlmostEqual(conversion1[0],6.4031242374328485)
        self.assertAlmostEqual(conversion1[1],0.8960553845713439)
    
    def test_polara_cartesiano(self):
        conversion2 = LC.polara_cartesianocomplex((6.4031242374328485, 0.8960553845713439))
        self.assertAlmostEqual(conversion2[0],4.0)
        self.assertAlmostEqual(conversion2[1],4.999999999999999)
    
    def test_fasecomplex(self):
        fase = LC.fasecomplex((4,5))
        self.assertAlmostEqual(fase,0.8960553845713439)


if __name__ == '__main__':
    unittest.main()

