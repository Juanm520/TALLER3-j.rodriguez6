import unittest
from models.Huron import Huron

class TestHuron(unittest.TestCase):
    def test_huron_sonido_correcto(self):
        huron = Huron("Pablo", 3.4, 2, "Canada", 31040.8)
        self.assertEqual(huron.hacer_sonido(), '¡Eek Eek!')

    def test_calcular_flete_correcto(self):
        huron = Huron("Pablo", 3.4, 2, "Canada", 31040.8)
        self.assertEqual(huron.calcular_flete(), 105538.72)
