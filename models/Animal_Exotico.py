from models.Animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos

    def calcular_flete(self) -> float:
        return round(self.__impuestos * self.peso, 2)
    
    @property
    def pais_origen(self):
        return self.__pais_origen
    @pais_origen.setter
    def pais_origen(self, nuevo_pais_origen:str) -> str:
        if isinstance(nuevo_pais_origen, str) and nuevo_pais_origen != '':
            self.__pais_origen = nuevo_pais_origen

    @property
    def impuestos(self):
        return self.__impuestos
    @impuestos.setter
    def impuestos(self, nuevo_impuesto: float) -> float:
        if isinstance(nuevo_impuesto, float) and nuevo_impuesto != '':
            self.__impuestos = nuevo_impuesto
