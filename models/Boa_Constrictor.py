from models.Animal_Exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0

    def hacer_sonido(self):
        return '¡Tsss!'
    
    def comer_raton(self) -> None:
        if self.__ratones_comidos == 10:
            raise ValueError('Demasiados Ratones!')
        self.__ratones_comidos += 1

    @property
    def ratones_comidos(self):
        return self.__ratones_comidos
    