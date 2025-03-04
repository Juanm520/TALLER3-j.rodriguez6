import unittest
from models.Boa_Constrictor import Boa_Constrictor

class TestBoa(unittest.TestCase):
    def test_sonido_de_boa(self):
        boa = Boa_Constrictor('Filomena', 35.0, 8, 'Peru', 34500.3)
        self.assertEqual(boa.hacer_sonido(), '¡Tsss!')
    
    def test_calcular_flete_correcto(self):
        boa = Boa_Constrictor('Filomena', 35.0, 8, 'Peru', 34500.3)
        self.assertEqual(boa.calcular_flete(), 1207510.5)
    
    def test_comer_correctamente(self):
        boa = Boa_Constrictor('Filomena', 35.0, 8, 'Peru', 34500.3)
        boa.comer(5.0)
        self.assertEqual(boa.obtener_kilos_comidos(), 5.0)
    