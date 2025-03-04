from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def comer(self, kilos) -> None:
        pass

    @abstractmethod
    def obtener_kilos_comidos(self) -> float:
        pass