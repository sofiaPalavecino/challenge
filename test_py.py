import unittest
import escalera
import productos
from productos import *


class Test(unittest.TestCase):
    def testEscalera(self):
        self.assertEqual(escalera.soluciones(6),13, "Debería ser 13")
        self.assertEqual(escalera.fibonacci(5),5, "Debería ser 5")

    def testProductos(self):
        producto1 = Product(105, "pelota")
        producto2 = Product(106, "lapiz")
        producto3 = Product(107, "libro")

        compra1 = Purchase("B001-002310",datetime.strptime("2019-07-01",'%Y-%m-%d'),[producto1, producto2])
        compra2 = Purchase("B001-002310",datetime.strptime("2019-07-02",'%Y-%m-%d'),[producto1, producto3])
        compra3 = Purchase("B001-002310",datetime.strptime("2019-11-03",'%Y-%m-%d'),[producto1, producto2])
        compra4 = Purchase("B001-002310",datetime.strptime("2020-07-04",'%Y-%m-%d'),[producto1, producto3])
        compra5 = Purchase("B001-002310",datetime.strptime("2021-01-15",'%Y-%m-%d'),[producto1, producto3])

        self.assertEqual(productos.getFrecuencia(compra2.date,compra1.date),1, "El test 1 de getsFrecuencia falló")
        self.assertEqual(productos.getFrecuencia(compra5.date,compra3.date),439, "El test 2 de getsFrecuencia falló")
        self.assertEqual(productos.getFrecuencia(compra5.date,compra5.date),0, "El test 3 de getsFrecuencia falló")

        self.assertEqual(productos.detectAtypical([1,2,3,1,2,10]),[10], "El test 1 de detectAtypical falló")
        self.assertEqual(productos.detectAtypical([1,2,3,1,2,700]),[700], "El test 2 de detectAtypical falló")
        self.assertEqual(productos.detectAtypical([1,2,3,1,2,10,600,601,602,603]),[], "El test 3 de detectAtypical falló")
        

if __name__ == "__main__":
    unittest.main()