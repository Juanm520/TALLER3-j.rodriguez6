from abc import ABC, abstractmethod
from models.IAnimal import IAnimal

class Animal(IAnimal, ABC):
    def __init__(self, nombre: str, peso: float, edad: int):
        self.__nombre = nombre
        self.__peso = peso
        self.__edad = edad
        self.__kilos_comidos = 0.0

    def comer(self, kilos: float):
        self.__kilos_comidos += kilos

    def obtener_kilos_comidos(self):
        return round(self.__kilos_comidos, 2)
    
    @abstractmethod
    def hacer_sonido(self):
        pass

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> str:
        if isinstance(nuevo_nombre, str) and nuevo_nombre != '':
            self.__nombre = nuevo_nombre

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, nuevo_peso:float) -> float:
        if isinstance(nuevo_peso, float) and nuevo_peso != '':
            self.__peso = nuevo_peso
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, nueva_edad:int) -> int:
        if isinstance(nueva_edad, int) and nueva_edad != '':
            self.__edad = nueva_edad
    
    


