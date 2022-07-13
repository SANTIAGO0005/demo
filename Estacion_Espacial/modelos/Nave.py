from abc import ABC,abstractmethod

class nave(ABC):

    @abstractmethod
    def __init__(self,nombre,peso,altura,comustible,potencia,estado):
            self._nombre = nombre
            self._peso = peso
            self._altura = altura
            self._combustible = comustible
            self._potencia = potencia
            self._estado = estado

    @abstractmethod
    def crear_nave(self):
            pass

    @abstractmethod
    def encender_nave(self):
            pass

    @abstractmethod
    def apagar_nave(self):
        pass

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor