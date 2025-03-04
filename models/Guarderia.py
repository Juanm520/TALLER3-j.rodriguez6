from models.Boa_Constrictor import Boa_Constrictor
from models.Huron import Huron

class Guarderia:
    def __init__(self):
        self.__boa1 = Boa_Constrictor('Filomena', 35.0, 8, 'Peru', 34500.3)
        self.__boa2 = Boa_Constrictor('Filomeno', 40.0, 9, 'Brasil', 36534.56 )
        self.__huron1 = Huron('Pablo', 3.4, 2, 'Canada', 31040.8)
        self.__huron1 = Huron('Patricia', 4.2, 4, 'Canada', 31040.8)

    def alimentar_boa(self, nombre: str) -> None:
        if nombre == self.__boa1.nombre:
            boa = self.__boa1
        elif nombre == self.__boa2.nombre:
            boa = self.__boa2
        else:
            raise ValueError('Esta Boa no existe')
        try:
            boa.comer_raton()
        except Exception:
            raise ValueError('La boa está llena')
        return 'Éxito'
    